#coding=utf-8  
  
import os
import shutil

if __name__ == '__main__':
    oldpath = os.getcwd()
    print (oldpath)
    newpath=oldpath+'/newpath'
    i= 1
    while  i < 1501:
        shutil.copy('case.xml', newpath)
        newfileName='case'+str(i)+'.xml'
        #判断文件是否存在,若不存在就改名
        if not os.path.exists(newpath+'/'+newfileName):
            print (i)
            os.rename(os.path.join(newpath,'case.xml'),os.path.join(newpath,newfileName))
        i+=1
