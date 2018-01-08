# _*_ coding:utf-8 _*_
import jenkins,time,os
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
url='http://10.10.11.8:8080'
user=input('Please input username:')
pwd=input('Please input password:')
job='Tester_4ALL'
def project_built(server, project_name, parameter): #这个函数作用是构建项目          
    server.build_job(project_name, {'test-parameter': parameter})  
    #等待构建完成
    jenkinsapi.api.block_until_complete(url,[job], maxwait=120, interval=5, raise_on_timeout=True, username=user, password=pwd, ssl_verify=True)
    
def printfile(buildinfo):
    #print (buildinfo)
    #print (buildinfo['artifacts'])
    print ('All build files:')
    for file in buildinfo['artifacts']:
        print (file['fileName'])    
def printBuilduser(buildinfo):
    print ('Build user is:'+buildinfo['actions'][1]['causes'][0]['userId'])
    
def printBuildDate(buildinfo):
    timeStamp = buildinfo['timestamp']
    #timeStamp=buildinfo.get_timestamp()
    timeArray = time.localtime(timeStamp/1000)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print ('Build date is:'+otherStyleTime)
  
def printBuildTime(buildinfo):
    print ('Build time is:%s'%(buildinfo['estimatedDuration']))
def getlastBuild(server):
    buildnumber=server.get_job_info(job)['lastBuild']['number']
    print ('BuildNumber is:%s'%(buildnumber))
    return buildnumber
def get_Status(buildnumber):
    status=server.get_build_info(job,buildnumber)['result']
    print ('Build status is :%s'%(status))
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

def grab_artifact(jobname,buildnumber, targetdir,strict_validation=False, ssl_verify=True):
    artifacts = get_artifacts(jobname,buildnumber,ssl_verify=ssl_verify)
    #artifact = artifacts[artifactid]
    for key,value in artifacts.items():
        if not os.path.exists(targetdir):
            os.makedirs(targetdir)
        value.save_to_dir(targetdir, strict_validation)
        file=os.path.join(targetdir,key)
        filesize=os.path.getsize(file)
        print ('%s:%s bytes'%(key,filesize))
if __name__ == '__main__':
    try:
        server = jenkins.Jenkins(url,user,pwd) 
    except Exception:
        print ('login jenkins failed!')
      
    project_built(server,job,user)
    buildnumber=getlastBuild(server)
    if get_Status(buildnumber)=='SUCCESS':
        buildinfo=server.get_build_info(job,buildnumber)
        printBuilduser(buildinfo)
        printBuildDate(buildinfo)
        printBuildTime(buildinfo)
        grab_artifact(job,buildnumber, './download',strict_validation=False, ssl_verify=True)
       
        

    
    
 
    
    
    
        

    