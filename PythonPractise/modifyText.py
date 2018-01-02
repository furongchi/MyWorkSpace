# coding:utf8
# _*_ coding:utf-8 _*_
import os
oldText="Snapshot"
newText="snapshot"
path="C:\\Users\\furongchi\\workspace\\Test\\TestCase"
num=0

actionList={"ImageCompareMultiBenchmark","ImageCompareExcludeArea","ImageCompareMultiArea"}
def listFile(filepath):
    global num
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            listFile(fi_d)
        else:
            #print (fi)
            #replaceText(os.path.join(filepath,fi_d))
            num=num+1
            findLastParam(os.path.join(filepath,fi_d))
            
        
def findLastParam(file):
    flag=False
    f = open(file,mode='r+',encoding='UTF-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        if "last" in line:
            if flag==True :
                print (line)
                tmpStr=line.strip()
                newStr="<!--"+tmpStr+"-->"
                line = line.replace(tmpStr,newStr)
                flag=False
        else:
            for a in actionList:
                if a in line:
                    print(file)
                    flag=True
                    break
        f.write(line)
    f.close()
            
    
            
def replaceText(file):
    f = open(file,mode='r+',encoding='UTF-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        line = line.replace(oldText,newText)
        f.write(line)
    f.close()
    
if __name__ == '__main__':
    listFile(path)
    print (num)