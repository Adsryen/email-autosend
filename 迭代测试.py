fileopen = open('C:\\Users\\Administrator\\Desktop\\邮件自动化\\receiver.txt', encoding='utf-8')
receivers = fileopen.readlines()

for receiver in receivers:
    '''receiver = line.strip('\n') #去掉换行符'''
    print(receiver)