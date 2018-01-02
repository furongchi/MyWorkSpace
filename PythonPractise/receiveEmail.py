#coding=utf-8
#-*- encoding:gbk -*-
import poplib
import email
from email.parser import Parser
from email.header import decode_header,Header
from email.utils import parseaddr

smtpserver= 'pop.263.net'
user=input('Please input 263 Email address:')
password=input('Please inout Email password:')
pop=None

def loginEmail():
    global pop
    try:
        pop = poplib.POP3(smtpserver)
        print(pop.getwelcome())
        pop.user(user)
        pop.pass_(password)
    except poplib.error_proto:
        print('login failed')


def getEmailNumber():
    eNumber=len(pop.list()[1])
    print ("Total Email number:%d"%eNumber)
    return eNumber

def getMsg(num):
    lines=pop.retr(num)[1]
    for i in range(0, len(lines)):
        lines[i] = bytes.decode(lines[i])
    #msg = email.message_from_string('\n'.join(lines))
    msg_content = '\r\n'.join(lines)
    msg = Parser().parsestr(msg_content)
    return msg


def getHeader(num):
    response, lines, octets = pop.top(num , 0)
    #把byte类型转换成字符串
    for i in range(0, len(lines)):
            lines[i] = bytes.decode(lines[i])
    #把信息转换成邮件类型

    header=email.message_from_string('\n'.join(lines))
    return header

'''def printHeader(headerMsg):
    for header in 'From', 'To','CC','Subject', 'Date':
        if header in headerMsg:
            content = headerMsg[header]
            content=decode_header(content)
            print(header + ':',content )'''

def printHeader(indent,msg):
    for header in ['From', 'To','CC', 'Subject']:
            pvalue=''
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    pvalue=decode_str(value)
                else:
                    contactlist=value.split(',')
                    for contact in contactlist:
                        hdr, addr = parseaddr(contact)
                        name=decode_str(hdr)
                        pvalue =pvalue+ u'%s <%s>' % (name, addr)+','
                    pvalue=pvalue.strip(',')
            print('%s%s: %s' % ('  ' * indent, header, pvalue))

def printSize(emailNum):
    listing=pop.list()[1][emailNum-1]
    number, size = listing.split()
    number=bytes.decode(number)
    size=bytes.decode(size)
    print ('Message:'+number,'Size:'+size)

def printContent(msg,indent):
    if indent == 0:        # 邮件的From, To, Subject存在于根对象上:
        printHeader(indent,msg)
    #判断邮件是否是MIMEMultipart
    if (msg.is_multipart()):
        #返回所有子对象
        parts = msg.get_payload()
        #循环打印出每个子对象
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            #判断每个子对象是否是MIMEMultipart，并递归打印每一个子对象:
            printContent(part, indent + 1)
    else: # 邮件对象不是一个MIMEMultipart,
        filename=msg.get_filename()
        content = msg.get_payload(decode=True)
        #判断是否是附件
        if filename:
            filename=decode_str(filename)
            print('%sAttachment:%s' % ('  ' * indent,filename))
            fEx = open("%s"%(filename), 'wb')  
            fEx.write(content)  
            fEx.close()  
        else:
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content))
       
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset).strip()
    return value

def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        #print ("conten_type_guess is:"+content_type)
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
            #print ("charset is :"+charset)
    return charset

if __name__ == '__main__':
    loginEmail()
    emailNum=getEmailNumber()
    headerMsg=getHeader(emailNum)
    msg=getMsg(emailNum)
    #Print message size
    printSize(emailNum)
    #Print message content
    printContent(msg,0)
    # logout
    pop.quit()
