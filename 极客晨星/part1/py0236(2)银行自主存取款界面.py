# coding=utf-8
'''
课件
'''
# 用列表存储用户的信息（每一个字典就是一个用户的信息）
Account = [{'Name': 'Jack', 'Password': '123456', 'Balance': 3000},
           {'Name': 'Nancy', 'Password': '234567', 'Balance': 4000},
           {'Name': 'Mandy', 'Password': '345678', 'Balance': 2000},
           {'Name': 'Kimmy', 'Password': '456789', 'Balance': 5000}]

# 定义主界面函数
def home_page():
    print('='*20 + '欢迎使用伊海迪银行ATM自助存取款系统' + '='*20)
    print('''
                            1. 登录账号
                            2. 注册账号
                            3. 退出系统
    ''')
    print('=' * 20 + '欢迎使用伊海迪银行ATM自助存取款系统' + '=' * 20)

# 获取数据库中用户名和密码，存入list1_username，list2_password
def name():
    global list1_username
    global list2_password
    list1_username = []
    list2_password = []
    for j in range(len(Account)):
        all_username = Account[j]['Name']
        list1_username.append(all_username)  # 将遍历出来的用户存到列表
        all_password = Account[j]['Password']
        list2_password.append(all_password)  # 将遍历出来的密码存到列表

# 定义登陆函数
def user_login():
    name()
    username = input('请输入您的用户名：')
    password = input('请输入6位用户密码：')
    if username in list1_username and password in list2_password:
        for i in range(len(Account)):
            # 用户名和密码匹配一致，执行
            if username == Account[i]['Name'] and password == Account[i]['Password']:
                print( ' '*30+'*'+'您好 %s' % Account[i]['Name']+'*'+' '*30)
                break
        else:
            print('用户名和密码不一致，重新输入!')

    else:  # 密码和用户输入错误
        print('用户名没有注册!')
        input('>>按确定键返回主菜单<<')
        judge1()

#定义一个实现用户注册的函数
def new_account():
    name()
    while True:
        # 设置新用户名添加到用户库
        while True:
            new_username = input('请输入您的用户名：')
            if new_username in list1_username:
                print('用户名已存在，请重新输入！')
            elif new_username == '':
                print('用户名不能为空，请重新输入！')
            else:
                new_user = {'Name': new_username}
                Account.append(new_user)
                break
        while True:
            new1_password = input('请输入您的6位数字密码：')
            new2_password = input('请再次输入您的6位数字密码：')
            if new1_password == '' and new2_password == '':
                print('密码不能为空，请重新输入！')
            elif new1_password == new2_password:
                if len(new2_password) == 6 and new2_password.isdigit():
                    new_user['Password'] = new2_password
                    print('***恭喜您，新账户注册成功！***')
                    break
                elif len(new2_password) != 6:
                    print('密码长度不正确，请重新输入！')
                elif len(new2_password) == 6 or new2_password.isdigit():
                    print('密码不是纯数字密码，请重新输入')
            elif new1_password != new2_password:
                print('两次输入密码不一致，请重新输入！')
        # 新用户预存金额
        select = input('是否需要预存金额，需要请输入“1”后按确认键：')
        if select == '1':
            new_balance = int(input('请输入您预存金额：'))
            new_user['Balance'] = new_balance
            print('预存款成功！存款金额为：%d' % new_balance)
            input('>>按确定键返回主菜单<<')
            break
        else:
            input('>>按确定键返回主菜单<<')
            break

# 定义主界面判断函数
def judge1():
    while True:
        home_page()  # 主界面（主菜单函数）
        judge_1 = input('请选择您需要的服务：')
        if judge_1 == '1':
            user_login()  # 执行用户的登陆
        elif judge_1 == '2':
            new_account()
            judge1()
        elif judge_1 == '3':
            print('感谢您的使用，欢迎再次光临！')
            input('>>按确定键退出服务<<')
            break
        else:
            print('请输入选项中的有效数字！')
            input('>>按确定键继续为您服务<<')

judge1()