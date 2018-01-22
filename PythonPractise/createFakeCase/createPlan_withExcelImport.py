# _*_ coding:utf-8 _*_
import xlrd
from xlutils.copy import copy
preCaseName='Case_'
caseNumber=10000
pretaskName='task_'
caseNumPerTask=20
class Plan(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.old_excel = xlrd.open_workbook('./TestPlanImportTemplate.xls', formatting_info=True)
        self.new_excel = copy(self.old_excel)
        self.ws = self.new_excel.get_sheet(2)  
    
    def writeCaseToExcel(self):
        for i in range(caseNumber):
            caseId=preCaseName+str(i)
            self.ws.write(i+1,1,caseId)
        
    def writeTaskToExcel(self): 
        for i in range(int(caseNumber/20)):
            taskName=pretaskName+str(i)
            rowIndex=20*i
            for i in range(20):
                row=rowIndex+i
                self.ws.write(row+1,0,taskName)
            
    def saveExcel(self):
        self.new_excel.save('./TestPlanImportTemplate.xls')
        
if __name__ == '__main__':
    planobject=Plan()
    planobject.writeCaseToExcel()
    planobject.writeTaskToExcel()
    planobject.saveExcel()