# coding:utf8
# _*_ coding:utf-8 _*_
import os
import xlrd  
from xlutils.copy import copy  
preList=['ea-app-normal','ea-neof-normal','ea-usbrelay-normal','ea-vr-normal','ea-oss-normal','ea-esbd-J5','ea-esbd-J6','ea-iph-normal','ea-comp1-coolpad','ea-comp2-huawei',
                  'ea-sd-navigation','ea-sd-songs','ea-bt-coolpad','ea-carp-normal','ea-ampere-normal','ea-ecrd-normal','ea-usb-songs']
actiondict={preList[0]:['Android Auto'],
            preList[1]:['SendCANMSG','SendLINMSG','IgnitionControl','OnStarCall','EndPerdCANMSG'],
            preList[2]:['IgnitionControl','PowerRelay'],
            preList[3]:['RecVoiceCheck'],
            preList[4]:['OnStar'],
            preList[5]:['StartCaptureVIPLog'],
            preList[6]:['WriteMessageToSerialPort'],
            preList[7]:['IPhoneControl'],
            preList[8]:['Recipient','REFNumber','REFNumber2'],
            preList[9]:['Recipient2','REF2Number','REF2Number2'],
            preList[10]:['_nav','navigation'],
            preList[11]:['TEST-SD'],
            preList[12]:['call_611.wav','call_jacky.wav','call_Michael.wav','call_Steve.wav','dial_cmcc.wav','show_me_voice_keypad.wav','call_CMCC.wav','call_cmcc.wav','CMCC.wav',
                         'number.wav','call_Black.wav','functionId":"702"'],
            preList[13]:['Apple CarPlay'],
            preList[14]:['CheckAmpere'],
            preList[15]:['StartRecordVideo'],
            preList[16]:['TEST-USB1']
        }
path="C:\\Users\\furongchi\\workspace\\Test\\TestCase\\to_tms"
num=0
def listFile(filepath):
    global num
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            listFile(fi_d)
        else:
            num=num+1
            writeExcel(fi,0)
            writeExcel(filepath,1)
            print (os.path.join(filepath,fi_d))
            setPre(os.path.join(filepath,fi_d))    
            
def writeExcel(string,column):
    old_excel = xlrd.open_workbook('SetPre2.xls', formatting_info=True)  
    new_excel = copy(old_excel)  
    ws = new_excel.get_sheet(0)
    ws.write(num, column,string)
    new_excel.save('SetPre2.xls')
            
def setPre(file):  
    flag=False
    casePrelist=[] 
    f = open(file,mode='r+',encoding='UTF-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        for preItem in preList:
            for actionItem in actiondict[preItem]:
                if actionItem in line:
                    flag=True
                    print (preItem)
                    casePrelist.append(preItem)
                    break
            if flag:
                break
        f.write(line)
    f.close() 
    #remove duplicate items
    casePrelist=set(casePrelist)
    preContent = ",".join(casePrelist)
    print (preContent)
    writeExcel(preContent,2)

    
if __name__ == '__main__':
    listFile(path)
    print (num)