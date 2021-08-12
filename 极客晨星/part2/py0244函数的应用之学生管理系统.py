# coding=utf-8
'''
课件
'''


# 定义显示系统页面
def print_menu():
    print('-' * 20)
    print('''
    学生管理系统V1.0
    1. 添加学生
    2. 删除学生
    3. 修改学生
    4. 查询学生
    5. 显示所有学生
    6. 退出系统
    ''')
    print('-' * 20)

# 增加学生
info_list = []
def add_new_info():
    '''添加学生信息'''
    global info_list
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')
    new_qq = input('请输入QQ：')
    for temp_info in info_list:
        if temp_info['name'] == new_name:
            print('此用户名已经被占用，请重新输入')
            return
    info = {}
    info['name'] = new_name
    info['tel'] = new_tel
    info['qq'] = new_qq
    info_list.append(info)

# 删除学生
def del_info():
    '''删除学生信息'''
    global info_list
    del_num = int(input('请输入要删除的序号：'))
    if 0 <= del_num < len(info_list):
        del_flag = input('确定删除？（yes or no）：')
        if del_flag == 'yes':
            del info_list[del_num]
    else:
        print('输入序号有误，请重新输入')

# 查询学生
def search_info():
    '''查询学生信息'''
    search_name = input('请输入要查询的学生姓名：')



# 主程序
def main():
    '''用来控制整个流程'''
    while True:
        # 1. 显示系统页面
        print_menu()
        # 2. 获取用户的选择
        num = input('请输入要进行的操作(数字):')
        # 3. 根据用户选择，执行相应操作
        if num == '1':
            add_new_info()
        elif num == '2':
            del_info()
        elif num == '3':
            modify_info()
        elif num == '4':
            search_info()
        elif num == '5':
            print_all_info()
        elif num == '6':
            exit_flag = input('亲，你确定要退出么？(yes or no)')
            if exit_flag == 'yes':
                break

