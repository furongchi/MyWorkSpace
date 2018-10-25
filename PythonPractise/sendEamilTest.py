#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

smtpserver= 'smtp.263.net'
user=input('Please input user:')
password=input('Please input password:')
receiver=input('please input receiver:')
to_list=[receiver]


def send_mail():
    subject='我是XXX，这个我通过python发送的邮件'
    part1='你好,我是XXX，这个我通过python发送的邮件'
    msg = MIMEMultipart('related')
    msg['From'] = user 
    msg['To'] = ";".join(to_list) 
    msg['Subject']=Header(subject,'utf-8')
    msgText=MIMEText(part1,'html','utf-8')
    #Add text
    msg.attach(msgText)
    #msg.attach(addimg("a.png",'<image1>'))
    #Add attachment
    msg.attach(addAttachment("sendEamilTest.py"))
    msg.attach(addHtml())
    

    try:
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(user,to_list, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:  
        print (str(e))  
        return False
def addHtml():
    
        html = """
         <html> 
           <head></head> 
           <body>
           <ul>
           <li><a href="http://10.10.11.51:8000/picture/Koala.jpg">这是一个多媒体内容</a></li>
           </ul>
           </body>
         </html> 
        """
        part2=MIMEText(html, "html", "utf-8")
        return part2
                    
def addimg(src,imgid):
        fp = open(src, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', imgid)
        return msgImage
def addAttachment(src):
    attachment = MIMEText(open(src, "rb").read(), "base64", "utf-8")
    attachment["Content-Type"] = "application/octet-stream"
    attachment["Content-Disposition"] = "attachment; filename=\"furongEmailPrc.py\""
    return attachment
    
    
    
if __name__ == '__main__':
    if send_mail():
        print ("Send successfully")
    else:
        print ("Fail to send email")