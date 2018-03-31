# _*_ coding:utf-8 _*_
import jenkins,os,io
#import pycurl
import configparser
from requests.auth import HTTPBasicAuth
import jenkinsapi,requests
from jenkinsapi.jenkins import Jenkins
data={'sql':['mat-createtbls-mysql.sql','mat-createcust-mysql.sql'],
      'app':['mat.ear','mataweb.ear','matiweb.ear','matsweb.ear','ces.ear','cessweb.ear','jga.ear','jgasweb.ear'],
      'migratesql':[]}
localFolder='./'
class TMS_Deploy(object):
    '''
    classdocs
    '''
    artifacts=None
    fileSize_location={}
    fileSize_Jenkins={}
    fileSize_location_1={}

    def __init__(self):
        '''
        Constructor
        '''
        self.readConfig()
       
        try:
            self.server=jenkins.Jenkins(self.url,self.user,self.pwd)
        except Exception as e:
            print (e)  
    def project_build(self):       
        self.server.build_job(self.job)  
        jenkinsapi.api.block_until_complete(self.url,[self.job], maxwait=240, interval=5, raise_on_timeout=True, username=self.user, password=self.pwd, ssl_verify=True)
            
    def get_lastBuild(self,job):
        buildnumber=self.server.get_job_info(job)['lastBuild']['number']
        print ('BuildNumber is:%s'%(buildnumber))
        return buildnumber
    
    def get_Status(self,buildnumber):
        status=self.server.get_build_info(self.job,buildnumber)['result']
        print ('Build status is :%s'%(status))
        return status
    
    def get_artifacts(self):
        artifacts=jenkinsapi.api.get_artifacts(self.url, jobid=self.job, build_no=buildnumber, username=self.user, password=self.pwd, ssl_verify=True)
        return artifacts
    
    def get_grapArtifact(self,artifactid,targetdir):
        jenkinsapi.api.grab_artifact(self.url, self.job, artifactid, targetdir, username=None, password=None, strict_validation=False, ssl_verify=True)
        
    def get_build(self,build_no,jobid):
        build=jobid.get_build(build_no)
        return build
    
    def get_job(self):
        jenkinsci = Jenkins(self.url, self.user, self.pwd,ssl_verify=True)
        jobid = jenkinsci[self.job]
        return jobid
    
    def download(self,filename,targetdir,file_url):
        #print (artifact.get_data())
        #artifact=self.artifacts[filename]
        #artifact.save_to_dir(targetdir, strict_validation=False)
        r=requests.get(file_url, auth=HTTPBasicAuth(self.user, self.pwd),allow_redirects = True)
        filesize=r.headers['content-length']
        self.fileSize_Jenkins[filename]=filesize
        #print ("content-length:",r.headers['content-length'])
        #print("content-type:",r.headers['Content-Type'])
        with open(os.path.join(targetdir,filename), "wb") as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

    def search_migrateSql(self):
        for (key, value) in self.artifacts.items():
            if key.startswith('mat_migrate_2018'):
                data['migratesql'].append(key)
        print ("migrateSql:",data.get('migratesql'))
        
        
            
    def downloadFile(self,buildnumber):
        #download mysql,migrate,ear
        for (key, value) in data.items():
            targetdir='%s/%s/%s/%s'%(localFolder,self.job,buildnumber,key)
            if not os.path.exists(targetdir):
                os.makedirs(targetdir)
            for filename in value:
                artifact = self.artifacts[filename]
                if artifact:
                    print (filename,":\n",artifact)
                    
                    if key=='app':
                        fileUrl='%sview/All/job/%s/%s/artifact/systems/mats/appprod/tasmib/%s'%(self.url,self.job,buildnumber,filename)
                    else:
                        fileUrl=self.get_artifactsURL(artifact)
                    print("fileUrl:",fileUrl)
                    self.download(filename, targetdir,fileUrl)
                else:
                    print ('no file :%s'%(filename))
        print("fileSize in jenkins:\n",self.fileSize_Jenkins)
             
       
        
    def locationfileszie(self,file):
        filesize=os.path.getsize(file)
        return filesize
        
    def get_fileSize_location(self):
        for (key, value) in data.items():
            if value!= None:
                for filename in value:
                    if os.path.exists('%s/%s/%s/%s'%(localFolder,self.job,buildnumber,key)+'/'+filename):
                        filesize=self.locationfileszie(os.path.join('%s/%s/%s/%s'%(localFolder,self.job,buildnumber,key),filename))
                        self.fileSize_location[filename]=filesize
                    else:
                        print ('%s is not downloaded,please check location and server'%(filename))
                        return False
        print ('location size:\n',self.fileSize_location)
        return True
            
    '''def get_Filesize_Jenkins(self):
        for filename in earPackageList+self.migrateSql:
            value=self.artifacts[filename]
            filesize=self.pycurl_get_file_size(value)
            if filesize >= 0:
                self.fileSize_Jenkins[filename]=filesize
            else:
                print ("%s doesn't exists or can't get its size"%(filename))
                return False
        print ('jenkins size:')
        print (self.fileSize_Jenkins)
        return True'''
            
    def get_artifactsURL(self,value):
        return str(value)[29:-1].strip()

    def pycurl_get_file_size(self,value):
        url=self.get_artifactsURL(value)
        curl=pycurl.Curl()
        curl.setopt(pycurl.VERBOSE,1)
        curl.setopt(pycurl.FOLLOWLOCATION,1)
        curl.setopt(pycurl.MAXREDIRS,5)
        curl.setopt(pycurl.USERPWD,"%s:%s"%(self.user,self.pwd))
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
    
    def locationfileszie_1(self,file):
        filesize=os.path.getsize(file)
        return filesize
        
    '''def get_fileSize_location_1(self):
        for filename in earPackageList+self.migrateSql:
            if os.path.exists('C:/cygwin64/home/furongchi/MATS-TMS-FEATURE/267_manuldownloaded'+'/'+filename):
                filesize=self.locationfileszie(os.path.join('C:/cygwin64/home/furongchi/MATS-TMS-FEATURE/267_manuldownloaded',filename))
                print (filesize)
                self.fileSize_location_1[filename]=filesize
            else:
                print ('%s is not downloaded,please check location and server'%(filename))
                return False
        print ('location_1 size:')
        print (self.fileSize_location_1)
        return True   '''   
    
    def compare_fileSize(self):
        for (key, value) in data.items():
            for filename in value:
                print(filename," in location:",self.fileSize_location[filename])
                print(filename," in jenkins:",self.fileSize_Jenkins[filename])
                if  float(self.fileSize_location[filename])!=float(self.fileSize_Jenkins[filename]):
                #if  self.fileSize_location[filename]!=self.fileSize_Jenkins[filename]:
                    print('%s size is not correct'%(filename))
                    return False
        return True
            
    def deploy(self,buildnumber):
        os.system("./start.sh %s %s"%(buildnumber,self.job))
        
    def readConfig(self):
        conf = configparser.ConfigParser()
        conf.read('./config.ini')      
        self.url = conf.get("section1", "JENKINS_URL")
        self.job=conf.get("section1", "JENKINS_JOB")
        self.user=conf.get("section1", "USER")
        self.pwd=conf.get("section1", "PASSWORD")
    

        
if __name__ == '__main__':
    tms=TMS_Deploy()
    read=input('build new version or download packages from existing build (Y/N)?:')
    if read=="Y" or read=="y" or read=="yes":
        tms.project_build()
        buildnumber=tms.get_lastBuild(tms.job)
    else:
        buildnumber=int(input("Please input build number:"))
    if tms.get_Status(buildnumber)== 'SUCCESS':
        tms.artifacts=tms.get_artifacts() #get all artifacts
        if tms.artifacts:
            tms.search_migrateSql()
            #print (tms.artifacts)
            tms.downloadFile(buildnumber)
            #if tms.get_fileSize_location() and tms.get_fileSize_location_1():
            if tms.get_fileSize_location():
                if tms.compare_fileSize():
                    print ('pass')
                else:
                    print ('failed to compare file size ')
            else:
                print ('failed to get file size')
        else:
            print ('No any artifact')
    else:
        print ("Build doesn't finished or built failed")
    tms.deploy(buildnumber)

                    
                    
            
    
    
                  
    
