import smtplib
import datetime
import time
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication

def send_mail(areceiver):
    # 设置邮箱服务器地址以及端口
    smtp_server = "smtp.qq.com"
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    # 发件人邮箱
    asender = "blyat@qq.com"
    # 收件人邮箱
    areceiver = areceiver
    # 抄送人邮箱
    acc = 'blyat@qq.com'
    # 邮件主题
    asubject = '新年快乐！'

    # 发件人地址
    from_addr = "blyat@qq.com"
    # 邮箱密码（授权码）
    password = "bewxkelaphsgbjfe"

    # 邮件设置
    msg = MIMEMultipart()
    msg['Subject'] = asubject
    msg['to'] = areceiver
    msg['Cc'] = acc
    msg['from'] = "Ryen"

    # 邮件正文内容
    body ='''
    <h1><font color="red"><b>2021祝你新年快乐！</b></font></h1>
    <br>
    
    <h3>    =>  <a href = 'https://www.opbe.top/newyear/'> buling </a>  <=    </h3>

    <br>
    <p>活到老，学到老！！</p>
    
    
    <p>知识就是力量           =>   <a href = 'https://www.opbe.top/'>  Blog  </a>   <=  （IP+1）</p>
    
    '''

    # 添加邮件正文:
    msg.attach(MIMEText(body, 'html', 'utf-8'))

    # 添加附件
    # 注意这里的文件路径是斜杠
    '''
    xlsxpart = MIMEApplication(open('C:/Users/zhangjunhong/Desktop/这是附件.xlsx', 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename='这是附件.xlsx')
    msg.attach(xlsxpart)
    '''

    # 登陆邮箱
    server.login(from_addr, password)
    # 当前时间
    now_time = datetime.datetime.now()
    #去掉输出日志时的邮件首尾自带的换行符
    areceiver_strip = areceiver.strip()
    # 发送邮件(日志生成在当前目录)
    try:
        server.sendmail(from_addr,areceiver.split(',') + acc.split(','), msg.as_string())
        print(areceiver + "邮件发送成功")
        with open(r'记录.log', 'a+') as f:
            f.write(areceiver_strip + "-----邮件发送成功------------------" + str(now_time) + '\n' + '\n')

    except smtplib.SMTPException:
        print(areceiver + "Error: 无法发送邮件")
        with open(r'记录.log', 'a') as f:
            f.write(areceiver_strip + "-----Error: 无法发送邮件------------------" + str(now_time) + '\n' + '\n')
    # 断开服务器链接
    '''server.quit()'''

#多个收件人文件列表（文件在同一目录下，不是同一目录需加' \\ ' ）
fileopen = open('receiver.txt', encoding='utf-8')
receivers = fileopen.readlines()
#遍历发送邮件
for receiver in receivers:
    '''receiver = line.strip('\n') #去掉换行符
    print(receiver)'''
    send_mail(receiver)
    #qq邮箱限制每日500封，每200秒发送一封
    time.sleep(200)

