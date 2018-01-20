# _*_ coding:utf-8 _*_
from jira import JIRA
import xlwt  
import logging
import datetime
url=' http://jira.odc.cienetcorp.com/'
projectName='MATSUP'
condition='project = MATSUP AND  status not in (Closed) AND updated <= "-1w" AND text ~ "SBT" ORDER BY created ASC'
user='furong_chi'
pwd='chi198318'
issues_list=[]
tamplate_title=['Project','IssueType','Key','Summary','Status','Reporter','Assignee','CreateTime','UpdateTime']
now = datetime.datetime.now().date()
searchFields='summary,description,comments'
class Jira(object):
    
    def __init__(self, serverurl,user,pwd):
        try:
            self.server=JIRA(serverurl,basic_auth=(user, pwd))
        except Exception as e:
            logging.exception(e)
            print ("login failed")
            
    def get_projects(self,projectName):
        project=None
        try:
            project = self.server.project(projectName)
            print (project.name)
        except Exception as e:
            logging.exception(e)
            print ('not find project:%s'%projectName)
        
        return project
    def search_issue_with_condition(self,condition,searchFields):
        #issues=self.server.search_issues(condition,maxResults = 100,expand='changelog',fields=searchFields,json_result ='True') #issues list is json data
        issues=self.server.search_issues(condition,fields=searchFields)
        return issues
    
    def setBackgroud(self,colour):
        pattern = xlwt.Pattern() # Create the Pattern
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern_fore_colour = colour # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
        return pattern 
    
    def write_title(self,style0):    
        for j in range(len(tamplate_title)):
                    self.ws.write(0,j,tamplate_title[j],style0)   
                    
    def write_row(self,row,issue):
        style0 = xlwt.XFStyle()
        updateTimeStr=issue[tamplate_title[-1]]
        updateTime=updateTimeStr[0:updateTimeStr.find('T')] #get str before "T"
        updateTime=datetime.datetime.strptime(updateTime, "%Y-%m-%d").date() #transfer str to datetime object
        #print (updateTime)
        #print((now-updateTime).days)
        if (now-updateTime).days >21:
            style0.pattern = self.setBackgroud(2) 
        for j in range(len(tamplate_title)):  
            self.ws.write(row,j,issue[tamplate_title[j]],style0)  
            
    def setWidth(self):
        for i in range(len(tamplate_title)):
            if tamplate_title[i]=='Summary':
                self.ws.col(i).width = 20000
            elif tamplate_title[i]=='Status':
                self.ws.col(i).width = 3000
            elif tamplate_title[i]=='CreateTime' or tamplate_title[i]=='UpdateTime':
                self.ws.col(i).width = 9000
            else:
                self.ws.col(i).width = 5000
                
                
            
    def writeIssueToExcel(self,issues_list):    
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('jira')
        self.setWidth()
        for i in range(len(issues_list)+1):
            style0 = xlwt.XFStyle()
            if i==0:
                style0.pattern = self.setBackgroud(4)
                self.write_title(style0)
                continue
            else:
                self.write_row(i,issues_list[i-1])     
        self.wb.save('Jira.xls') 
        
     
    def get_field(self,issue,field,issue_dict):
        fieldData=''
        if field=='Project':
            fieldData=issue.fields.project.name
            
        elif field=='IssueType':
            fieldData=issue.fields.issuetype.name

        elif field=='Key':
            fieldData=issue.key
            
        elif field=='Summary':
            fieldData=issue.fields.summary
           
        elif field=='Status':
            fieldData=issue.fields.status.name
           
        elif field=='Reporter':
            fieldData=issue.fields.reporter.displayName
          
        elif field=='Assignee':
            fieldData=issue.fields.assignee.displayName
           
        elif field=='Create':
            fieldData=issue.fields.created
        
        else:
            fieldData=issue.fields.updated  
           
        #print (fieldData)
        issue_dict[field]=fieldData
        return issue_dict 
    
if __name__ == '__main__':
    jira_object=Jira(url,user,pwd)
    project=jira_object.get_projects(projectName)
    if project != None:
        issues=jira_object.search_issue_with_condition(condition,searchFields)
        #print (issues)
        #issues.sort()
        #print (issues)
    if len(issues)>0:
        for issue in issues:
            #print ('description:'+issue.fields.description)
            #print (issue.id) 
            issue_dict={}
            issue=jira_object.server.issue(issue.key) #transfer issue object
            for i in range(len(tamplate_title)):
                #print (tamplate_title[i]+' is :')
                issue_dict=jira_object.get_field(issue,tamplate_title[i],issue_dict)
            #print (issue_dict)
            issues_list.append(issue_dict)
    #print (issues_list)         
            #print (issue.fields.comment.comments) #this is comments list
            #print (issue.fields.description)       
    jira_object.writeIssueToExcel(issues_list)

        
        
    
    
            
        
        
        
        