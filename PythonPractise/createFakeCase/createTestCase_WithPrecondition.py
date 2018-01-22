# _*_ coding:utf-8 _*_
import random
import xlrd
from xlutils.copy import copy  
preName='Precondition_'
PreCaseName='Case_'
preCasePath='preconditionTest/'
caseNumber=10000
totalPreNumber=100
PreNumPerCase=10

class createfakeCase(object):
    pre_list=[]
    preTypes=[]
    case_list={}

    def __init__(self):
        '''
        Constructor
        '''
    def create_precondition(self):
        for i in range(0,totalPreNumber):
            precondition=preName+str(i)
            self.pre_list.append(precondition)
    def getPre(self,PreNumPerCase):
        prelist=[]
        numlist=[random.randint(0,totalPreNumber-1) for _ in range(PreNumPerCase)]
        for i in range(len(numlist)):
            prelist.append(self.pre_list[numlist[i]])
        #print (numlist)
        prelist.sort()
        return prelist
        
    def create_caseDict(self):
        i=0
        while i < 50:
            print (i)
            preconditionList=self.setPreForCase(i)
            #print (preconditionList)
            for j in range(200):
                caseIndex=i*200
                caseId=PreCaseName+str(caseIndex+j)
                self.case_list[caseId]=preconditionList
            i=i+1
                        
    def writeCaseToExcel(self):
        old_excel = xlrd.open_workbook('./TestCaseImportTemplate.xls', formatting_info=True)
        new_excel = copy(old_excel)
        ws = new_excel.get_sheet(1)  
        for i in range(len(self.case_list)):
            caseId=PreCaseName+str(i)
            casePath=preCasePath+caseId+'.xml'
            prelist=",".join(self.case_list[caseId])
            ws.write(i+1,0,caseId)
            ws.write(i+1,1,casePath)
            ws.write(i+1,2,prelist)   
        new_excel.save('./TestCaseImportTemplate.xls')
        
    def setPreType(self):
        for i in range(0,50):
            firstNum=i
            endNum=totalPreNumber-1-i
            preType=[firstNum,endNum]
            if endNum-firstNum > 9:
                preType=preType+random.sample(range(firstNum+1,endNum), 8)
            elif endNum-firstNum > 1:
                preType=preType+random.sample(range(firstNum+1,endNum), endNum-firstNum-1)
            self.preTypes.append(sorted(preType))
            
    def setPreForCase(self,index):
        precondition=[]
        PreType=self.preTypes[index]
        for i in range(len(PreType)):
            precodtionName=preName+str(PreType[i])
            precondition.append(precodtionName)
        print (precondition)
        return precondition
                
            
if __name__ == '__main__':
    fake=createfakeCase()
    #fake.create_precondition()
    fake.setPreType()
    print (len(fake.preTypes))
    print (fake.preTypes)
    #print (fake.pre_list)
    fake.create_caseDict()
    #print (fake.case_list)
    fake.writeCaseToExcel()
 
    
        
    