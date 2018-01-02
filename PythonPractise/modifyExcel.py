#coding=utf-8 
import xlrd  
import xlwt  
from xlutils.copy import copy  
  
  

if __name__ == '__main__':
    old_excel = xlrd.open_workbook('TestPlanImportTemplate.xls', formatting_info=True)  
    new_excel = copy(old_excel)  
    ws = new_excel.get_sheet(2)  
    i=1
    index=1
    while i < 1501:
        j=0
        for j in range(10):
            taskName="task1103"+'_'+str(index)
            ws.write(i, 0, taskName)
            i+=1
            j+=1
            print (i)
        index+=1
    new_excel.save('new_fileName.xls')