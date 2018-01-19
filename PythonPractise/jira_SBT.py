# _*_ coding:utf-8 _*_
from jira import JIRA
import xlwt  
import logging
import datetime
url=' http://jira.odc.cienetcorp.com/'
projectName='MATSUP'
condition='project = MATSUP AND  status not in (Closed) AND updated <= "-1w" AND text ~ "SBT" ORDER BY created ASC'
user=input('Please input username:')
pwd=input('Please input password:')
issues_list=[]
tamplate_title=['project','issuetype','key','summary','status','reporter','assignee','create','update']

searchFields='summary,description,comments'
class Jira(object):
    
    def __init__(self, serverurl,user,pwd):
        #user=input('Please input username:')
        #pwd=input('Please input password:')
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
        for j in range(len(tamplate_title)):
            if tamplate_title[j]=='UpdateTime':
                now = datetime.datetime.now()
                print (now)
                print((now-tamplate_title[j]).days)
                if (now-tamplate_title[j]).days >21:
                    style0.pattern = self.setBackgroud(2)   
            self.ws.write(row,j,issue[tamplate_title[j]],style0)  
    def writeIssueToExcel(self,issues_list):    
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('jira')
        self.ws.col(0).width = 5000
        self.ws.col(1).width = 4000
        self.ws.col(2).width = 4500
        for i in range(len(issues_list)+1):
            style0 = xlwt.XFStyle()
            if i==0:
                style0.pattern = self.setBackgroud(4)
                self.write_title(style0)
                continue
            else:
                self.write_row(i,issues_list[i-1])
            
        self.wb.save('Jira.xls') 
if __name__ == '__main__':
    jira_object=Jira(url,user,pwd)
    project=jira_object.get_projects(projectName)
    if project != None:
        issues=jira_object.search_issue_with_condition(condition,searchFields)
        

        print (issues)
        #issues.sort()
        #print (issues)
    if len(issues)>0:
        i=0
        for issue in issues:
            issue_dic={}
            key=issue.key
            issue_dic['key']=key
            print ('key:'+key)
            summary=issue.fields.summary
            issue_dic['summary']=summary
            print ('summary:'+summary)
            #print ('description:'+issue.fields.description)
            #print (issue.id)   
            issue=jira_object.server.issue(issue.key)
            project=issue.fields.project.name
            issue_dic['project']=project
            print ('project is :%s'%(project))
            issuetype=issue.fields.issuetype.name
            issue_dic['issuetype']=issuetype
            print ('issuetype is :%s'%(issuetype))
            reporter=issue.fields.reporter.displayName
            issue_dic['reporter']=reporter
            print ('reporter is :%s'%(reporter))
            update=issue.fields.updated
            issue_dic['update']=update
            print('update time:%s'%(update))
            create=issue.fields.created
            issue_dic['create']=create
            print('created time is :%s'%(create))
            assignee=issue.fields.assignee.displayName
            issue_dic['assignee']=assignee
            print ('assignee is :%s'%(assignee))
            status=issue.fields.status.name
            issue_dic['status']=status
            print ('issue status is :%s'%(status))
            print (issue_dic)
            issues_list.append(issue_dic)

    print (issues_list)         
            #print (issue.fields.comment.comments) #this is comments list
            #print (issue.fields.description)
            
    jira_object.writeIssueToExcel(issues_list)

        
        
    
    
            
        
        
        
        