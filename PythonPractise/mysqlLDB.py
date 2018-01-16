# _*_ coding:utf-8 _*_
import MySQLdb
import io
precondition='./precondition.txt'

def get_precondition():
    preconditionList=[]
    f = io.open(precondition,mode='r+',encoding='UTF-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        #print (line)
        preconditionList.append(line.strip())
        f.write(line)
    return preconditionList
def delete_testcasepcmap(cursor,preconditioncode):
    sql='delete from mat_testcasepcmap where pcCode="%s"'%(preconditioncode)
    cursor.execute(sql)
    
def delete_devicepcmap(cursor,preconditioncode):
    sql='delete from mat_devicepcmap where pcCode="%s"'%(preconditioncode)
    cursor.execute(sql)
def delete_nodepcmap(cursor,preconditioncode):
    sql='delete from mat_nodepcmap where pcCode="%s"'%(preconditioncode)
    cursor.execute(sql)
    
def delete_pre(cursor,preconditioncode):
    sql='delete from mat_precondition where pcCode="%s"'%(preconditioncode)
    cursor.execute(sql)
    
def delete_pcmap(cursor,pcCode):
    delete_testcasepcmap(cursor,pcCode)
    delete_devicepcmap(cursor,pcCode)
    delete_nodepcmap(cursor,pcCode)
    
def delete(pcCode):
    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","root","mat20170907" )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    delete_pcmap(cursor,pcCode)
    delete_pre(cursor,pcCode)
    cursor.execute('commit')
    db.close()
    
def delete_precondition(precondtionList):
   
    for pcCode in precondtionList:
        delete(pcCode)

if __name__ == '__main__':
    precondtionList=get_precondition()
    delete_precondition(precondtionList)
    
    
