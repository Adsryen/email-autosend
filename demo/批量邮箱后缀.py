#后缀
suffix = '@qq.com'
#文件
fileopen = open('qq.txt', encoding='utf-8')
accounts = fileopen.readlines()

#遍历
for account in accounts:
    # 去掉输出时的首尾自带的换行符
    account_strip = account.strip()
    with open(r'email.txt', 'a+') as f:
        f.write(account_strip + suffix + '\n')
