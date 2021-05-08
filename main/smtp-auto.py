import smtplib
import datetime
import time
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication


#多个收件人文件列表1（文件在同一目录下，不是同一目录需加' \\ ' ）
fileopen = open('receiver.txt', encoding='utf-8')
receivers = fileopen.readlines()

#多个收件人文件列表2（文件在同一目录下，不是同一目录需加' \\ ' ）
fileopen_2 = open('receiver2.txt', encoding='utf-8')
receivers_2 = fileopen_2.readlines()

#多个收件人文件列表2（文件在同一目录下，不是同一目录需加' \\ ' ）
fileopen_3 = open('receiver3.txt', encoding='utf-8')
receivers_3 = fileopen_3.readlines()

def send_mail_1(areceiver):
    # 设置邮箱服务器地址以及端口
    smtp_server = "smtp.qq.com"
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    # 发件人邮箱
    asender = "blyat@qq.com"
    # 收件人邮箱
    areceiver = areceiver
    # 抄送人邮箱
    acc = ''
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
    <h1><font color="red"><b>迟到的新年快乐！</b></font></h1>
    <h1><font color="red"><b>Happy late New Year！</b></font></h1>
    <br>
    <h3>    =>  <a href = 'https://www.prlrr.com/newyear/'> buling </a>  <=    </h3>
    <br>
    <h3>    =>  <a href = 'https://www.prlrr.com/wallpaper-API/'> Pictures of the API </a>  <=    </h3>
    <br>
    <p>活到老，学到老！！-Never r too old to learn!！！</p>

    <p>知识就是力量-knowledge is power           =>   <a href = 'https://www.prlrr.com/'>  Blog  </a>   <=  （IP+1）</p>
    <br>
    <br>
    <p>于2月12日发送（可能存在网络延迟）</p>
    <p>Sent on February 12 (there may be network delay)</p>
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
        print(areceiver_strip + "-----1号--邮件发送成功")
        with open(r'记录.log', 'a+') as f:
            f.write(areceiver_strip + "-----1号--邮件发送成功------------------" + str(now_time) + '\n')

    except smtplib.SMTPException:
        print(areceiver_strip + "-----Error: 1号--无法发送邮件")
        with open(r'记录.log', 'a') as f:
            f.write(areceiver_strip + "-----Error: 1号--无法发送邮件------------------" + str(now_time) + '\n')
    # 断开服务器链接
    '''server.quit()'''

def send_mail_2(areceiver_2):
    # 设置邮箱服务器地址以及端口
    smtp_server = "smtp.qq.com"
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    # 发件人邮箱
    asender = "2960261139@qq.com"
    # 收件人邮箱
    areceiver = areceiver_2
    # 抄送人邮箱
    acc = ''
    # 邮件主题
    asubject = '新年快乐！'

    # 发件人地址
    from_addr = "2960261139@qq.com"
    # 邮箱密码（授权码）
    password = "iuaesprdbtmjdghf"

    # 邮件设置
    msg = MIMEMultipart()
    msg['Subject'] = asubject
    msg['to'] = areceiver
    msg['Cc'] = acc
    msg['from'] = "Ryen"

    # 邮件正文内容
    body = '''
    <h1><font color="red"><b>迟到的新年快乐！</b></font></h1>
    <h1><font color="red"><b>Happy late New Year！</b></font></h1>
    <br>
    <h3>    =>  <a href = 'https://www.prlrr.com/newyear/'> buling </a>  <=    </h3>
    <br>
    <h3>    =>  <a href = 'https://www.prlrr.com/wallpaper-API/'> Pictures of the API </a>  <=    </h3>
    <br>
    <p>活到老，学到老！！-Never r too old to learn!！！</p>

    <p>知识就是力量-knowledge is power           =>   <a href = 'https://www.prlrr.com/'>  Blog  </a>   <=  （IP+1）</p>
    <br>
    <br>
    <p>于2月12日发送（可能存在网络延迟）</p>
    <p>Sent on February 12 (there may be network delay)</p>
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
    # 去掉输出日志时的邮件首尾自带的换行符
    areceiver_strip = areceiver.strip()
    # 发送邮件(日志生成在当前目录)
    try:
        server.sendmail(from_addr, areceiver.split(',') + acc.split(','), msg.as_string())
        print(areceiver_strip + "-----2号--邮件发送成功")
        with open(r'记录.log', 'a') as f:
            f.write(areceiver_strip + "-----2号--邮件发送成功------------------" + str(now_time) + '\n')

    except smtplib.SMTPException:
        print(areceiver_strip + "-----Error: 2号--无法发送邮件")
        with open(r'记录.log', 'a') as f:
            f.write(areceiver_strip + "-----Error: 2号--无法发送邮件------------------" + str(now_time) + '\n')
    # 断开服务器链接
    '''server.quit()'''

def send_mail_3(areceiver_3):
        # 设置邮箱服务器地址以及端口
        smtp_server = "smtp.qq.com"
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        # 发件人邮箱
        asender = "rap.vip@qq.com"
        # 收件人邮箱
        areceiver = areceiver_3
        # 抄送人邮箱
        acc = ''
        # 邮件主题
        asubject = '新年快乐！'

        # 发件人地址
        from_addr = "rap.vip@qq.com"
        # 邮箱密码（授权码）
        password = "xfoytmiirbzcdhed"

        # 邮件设置
        msg = MIMEMultipart()
        msg['Subject'] = asubject
        msg['to'] = areceiver
        msg['Cc'] = acc
        msg['from'] = "Ryen"

        # 邮件正文内容
        body = '''
    <h1><font color="red"><b>迟到的新年快乐！</b></font></h1>
    <h1><font color="red"><b>Happy late New Year！</b></font></h1>
    <br>
    <h3>    =>  <a href = 'https://www.prlrr.com/newyear/'> buling </a>  <=    </h3>
    <br>
    <h3>    =>  <a href = 'https://www.prlrr.com/wallpaper-API/'> Pictures of the API </a>  <=    </h3>
    <br>
    <p>活到老，学到老！！-Never r too old to learn!！！</p>

    <p>知识就是力量-knowledge is power           =>   <a href = 'https://www.prlrr.com/'>  Blog  </a>   <=  （IP+1）</p>
    <br>
    <br>
    <p>于2月12日发送（可能存在网络延迟）</p>
    <p>Sent on February 12 (there may be network delay)</p>
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
        # 去掉输出日志时的邮件首尾自带的换行符
        areceiver_strip = areceiver.strip()
        # 发送邮件(日志生成在当前目录)
        try:
            server.sendmail(from_addr, areceiver.split(',') + acc.split(','), msg.as_string())
            print(areceiver_strip + "-----3号--邮件发送成功")
            with open(r'记录.log', 'a') as f:
                f.write(areceiver_strip + "-----3号--邮件发送成功------------------" + str(now_time) + '\n')

        except smtplib.SMTPException:
            print(areceiver_strip + "-----Error: 3号--无法发送邮件")
            with open(r'记录.log', 'a') as f:
                f.write(areceiver_strip + "-----Error: 3号--无法发送邮件------------------" + str(now_time) + '\n')
        # 断开服务器链接
        '''server.quit()'''

#多次遍历发送邮件
for receiver,receiver_2,receiver_3 in zip(receivers,receivers_2,receivers_3):
    ''' receiver = line.strip('\n') #去掉换行符
    print(receiver)'''
    send_mail_1(receiver)
    time.sleep(10)
    send_mail_2(receiver_2)
    time.sleep(10)
    send_mail_3(receiver_3)
    #qq邮箱限制每日500封，每200秒发送一封
    time.sleep(179)



