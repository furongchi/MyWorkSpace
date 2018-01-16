# _*_ coding:utf-8 _*_
import jenkins,time,os,io
import pycurl
import urllib.request  
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
from pip._vendor.requests.api import request
url='http://10.10.11.8:8080'
user=input('Please input username:')
pwd=input('Please input password:')
job='Tester_4ALL'
targetdir='./download'
f = open("out.txt", "w+")  
def project_built(server, project_name, parameter): #这个函数作用是构建项目          
    server.build_job(project_name, {'test-parameter': parameter})  
    #等待构建完成
    jenkinsapi.api.block_until_complete(url,[job], maxwait=120, interval=5, raise_on_timeout=True, username=user, password=pwd, ssl_verify=True)
    
def printfile(buildinfo):
    print (buildinfo)
    print (buildinfo['artifacts'])
    print ('All build files:')
    for file in buildinfo['artifacts']:
        print (file['fileName'])    
def printBuilduser(buildinfo):
    print ('Build user is:%s'%(buildinfo['actions'][1]['causes'][0]['userId']),file=f)
    
def printBuildDate(buildinfo):
    timeStamp = buildinfo['timestamp']
    #timeStamp=buildinfo.get_timestamp()
    timeArray = time.localtime(timeStamp/1000)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print ('Build date is:%s'%(otherStyleTime),file=f)
  
def printBuildTime(buildinfo):
    print ('Build time is:%s'%(buildinfo['estimatedDuration']),file=f)
def getlastBuild(server):
    buildnumber=server.get_job_info(job)['lastBuild']['number']
    print ('BuildNumber is:%s'%(buildnumber),file=f)
    return buildnumber
def get_Status(buildnumber):
    status=server.get_build_info(job,buildnumber)['result']
    print ('Build status is :%s'%(status),file=f)
    return status
def get_artifacts(jobname,buildnumber, ssl_verify=True):
    jenkinsci = Jenkins(url, user, pwd,ssl_verify=ssl_verify)
    job = jenkinsci[jobname]
    if buildnumber:
        build = job.get_build(buildnumber)
    else:
        build = job.get_last_good_build()
    artifacts = build.get_artifact_dict()
    return artifacts
def download_artifact(value,targetdir,strict_validation):
    #print (value.get_data())
    if not os.path.exists(targetdir):
        os.makedirs(targetdir)
    value.save_to_dir(targetdir, strict_validation)
def location_get_file_size(file):
    filesize=os.path.getsize(file)
    return filesize
def urllib_get_file_size(value,proxy=None):  
    url=get_artifactsURL(value)
    auth=urllib.request.HTTPBasicAuthHandler()
    auth.add_password('User',url,user,pwd)
    opener=urllib.request.build_opener(auth)
    if proxy:
        if url.lower().startswith('https://'):
            opener.add_handler(urllib.request.ProxyHandler({'https' : proxy}))
        else:
            opener.add_handler(urllib.request.ProxyHandler({'http' : proxy}))
    try:
       
        request = urllib.request.Request(url)
        #urllib.request.urlretrieve(url,fileName) #下载文件到本地
        #urllib.request.urlopen()
        request.get_method = lambda: 'HEAD'
        response = opener.open(request)
        response.read()
        
        
    except Exception as e: # 远程文件不存在        
        print (e)
        return -1
    else:
        return dict(response.headers).get('content-length', -1) #获取header里的content-length 
    
def pycurl_get_file_size(value):
    url=get_artifactsURL(value)
    curl=pycurl.Curl()
    curl.setopt(pycurl.VERBOSE,1)
    curl.setopt(pycurl.FOLLOWLOCATION,1)
    curl.setopt(pycurl.MAXREDIRS,5)
    curl.setopt(pycurl.USERPWD,"%s:%s"%(user,pwd))
    curl.setopt(pycurl.CONNECTTIMEOUT,60)
    curl.setopt(pycurl.TIMEOUT,300)
    curl.setopt(pycurl.HTTPPROXYTUNNEL,1)
    curl.setopt(pycurl.URL,url)
    
    try:
        curl.fp=io.BytesIO()
        curl.setopt(pycurl.WRITEFUNCTION,curl.fp.write)
        curl.perform()
        #response=curl.fp.getvalue()
        #print (response)
    except Exception as e:
        print (e)
        return -1
    return curl.getinfo(pycurl.CONTENT_LENGTH_DOWNLOAD)    

def get_artifactsURL(value):
    return str(value)[29:-1].strip()

def print_artifactName_and_size(key,filesize):
    print ('%s:%s bytes'%(key,filesize),file=f)
    
def download_artifact_and_get_file_size(artifacts,strict_validation=False):
    #artifact = artifacts[artifactid]
    print ("Print artifacts name and size:",file=f)
    for key,value in artifacts.items():
        #download_artifact(value,targetdir,strict_validation)
        #filesize=location_get_file_size(os.path.join(targetdir,key))
        #filesize=urllib_get_file_size(value,proxy=None)
        filesize=pycurl_get_file_size(value)
        if filesize>=0:
            print_artifactName_and_size(key,filesize)
        else:
            print ("Can't find artifact",file=f)     
              
if __name__ == '__main__':
    try:
        server = jenkins.Jenkins(url,user,pwd) 
    except Exception:
        print ('login jenkins failed!',file=f)     
    project_built(server,job,user)
    buildnumber=getlastBuild(server)
    if get_Status(buildnumber)=='SUCCESS':
        buildinfo=server.get_build_info(job,buildnumber)
        #printfile(buildinfo)
        printBuilduser(buildinfo)
        printBuildDate(buildinfo)
        printBuildTime(buildinfo)
        artifacts = get_artifacts(job,buildnumber,ssl_verify=True)
        if artifacts:
            download_artifact_and_get_file_size(artifacts,strict_validation=False)
        else:
            print ('No any artifact exists',file=f)
       
        

    
    
 
    
    
    
        

    