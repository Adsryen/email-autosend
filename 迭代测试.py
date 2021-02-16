fileopen = open('receiver.txt', encoding='utf-8')
receivers = fileopen.readlines()

for receiver in receivers:
    '''receiver = line.strip('\n') #去掉换行符'''
    print(receiver)
    with open(r'cesi记录.log', 'a+') as f:
        f.write(receiver + "-----邮件发送成功------------------"  + '\n' + '\n')
