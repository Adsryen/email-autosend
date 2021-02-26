#多个收件人文件列表1（文件在同一目录下，不是同一目录需加' \\ ' ）
fileopen = open('receiver.txt', encoding='utf-8')
receivers = fileopen.readlines()

#多个收件人文件列表2（文件在同一目录下，不是同一目录需加' \\ ' ）
fileopen_2 = open('receiver2.txt', encoding='utf-8')
receivers_2 = fileopen_2.readlines()

for receiver,receiver_2 in zip(receivers,receivers_2):
    '''receiver = line.strip('\n') #去掉换行符'''
    receiver_strip = receiver.strip()
    receiver_2_strip = receiver_2.strip()
    print(receiver_strip + '和' + receiver_2_strip)
