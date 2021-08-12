#coding=utf-8

# 存储的用户信息，列表形式，列表内元素为字典类型。
Account = [{'Name': 'Jack', 'Password': '123456', 'Balance': 3000},
           {'Name': 'Nancy', 'Password': '234567', 'Balance': 4000},
           {'Name': 'Mandy', 'Password': '345678', 'Balance': 2000},
           {'Name': 'Kimmy', 'Password': '456789', 'Balance': 5000}]


def home_page():
    '''
    程序首界面
    :return:
    '''
    print('=' * 20 + '欢迎使用朱楀墨银行ATM自助存取款系统' + '=' * 20)
    print('''
                            1. 登录账号
                            2. 注册账号
                            3. 退出系统
    ''')
    print('=' * 20 + '欢迎使用朱楀墨银行ATM自助存取款系统' + '=' * 20)

def name():
    global list1_username
    global list2_password
    list1_username = []
    list2_password = []
    for i in range(len(Account)):
        all_username = Account[i]['Name']
        list1_username.append(all_username)
        all_password = Account[i]['Password']
        list2_password.append(all_password)

def user_login():
    name()
    username = input('请输入您的用户名：')
    password = input('请输入您的密码：')
    if username in list1_username and password in list2_password:
        for i in range(len(Account)):
            if username == Account[i]['Name'] and password == Account[i]['Password']:
                print('{}您好，登录成功'.format(username))
                break
        else:
            print('用户名和密码不匹配！')
    else:
        print('用户没有被注册')
        input('请按回车键返回主菜单')
        judge()

def new_account():
    name()
    while True:
        while True:
            new_username = input('请输入您的用户名：')
            if new_username in list1_username:
                print('用户名已存在，请重新输入')
            elif new_username == '':
                print('用户名不能为空')
            else:
                new_user = {'Name':new_username}
                Account.append(new_user)
                break
        while True:
            new1_password = input('请输入6位数密码：')
            new2_password = input('请再次输入密码：')
            if new1_password == new2_password:
                pass
            elif new1_password != new2_password:
                print('两次输入密码不一致')

def judge():
    pass