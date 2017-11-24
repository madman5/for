# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# ------------------跟发件相关参数------------------------

# QQ
# smtpserver = "xxxx@qq.com"
# port = 465

# 163
smtpserver = "smtp.163.com"    # 发件服务器
port = 0                       # 端口
sender = "lfengwei5@163.com"   # 帐号
psw = "lfw5201314"             # 密码
receivew = ["277646315@qq.com","369873625@qq.com"]  # 接收帐号



# # -------------------编辑邮件的内容----------------------


# 不带附件

# subject = "主题"
# body = '<p>这是我发送的邮件<p>'

# msg = MIMEText(body, 'html', 'utf-8')
# msg['from'] = sender
# msg['to'] = receivew
# msg['subject'] = subject


# 带附件

# 附件绝对路径
filename = ("Report/2017-11-23_18_23_35.html")
with open(filename, mode = 'rb') as fh:
    mail_body = fh.read()

msg = MIMEMultipart()
msg['from'] = sender
msg['to'] = ";".join(receivew)
msg['subject'] = "自动化测试报告"
body = MIMEText(mail_body,'html','utf-8')

msg.attach(body)

att = MIMEText(mail_body,'base64','utf-8')
att['Content-Type'] = "application/octet-stream"
att['Content-Disposition'] = 'attachment;filename = "test_report.html"'
msg.attach(att)

# -----------------------发送邮件-------------------------

# QQ
# smtp = smtplib.SMTP_SSL(smtpserver,port)
# smtp.login(sender,psw)      # 登录
# smtp.sendmail(sender,receivew,msg.as_string())
# smtp.quit()

# 163
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)    # 连接服务器
# smtp.login(sender,psw)      # 登录
# smtp.sendmail(sender,receivew,msg.as_string())
# smtp.quit()



# 兼容QQ\163
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
    # smtp.sendmail(sender,receivew,msg.as_string())
except:
    smtp =smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender.psw)
smtp.sendmail(sender,receivew,msg.as_string())
smtp.quit()


