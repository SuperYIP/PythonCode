#coding=utf-8
# 课前
'''
吴博熠家长您好 很高兴给吴博熠同学上试听课 我们 19:30 准时见~ 若是有什么问题 我们随时沟通
“家长您好，可以进入课堂了 请点击”去上课””
已进入课堂
'''

# 课上
'''
自我介绍
    吴博熠同学 在课堂开始之前呢 老师做个自我介绍 老师姓伊 你可以叫我伊老师 老师是一名计算机专业在读研究生
现在也是我们极客晨星的编程老师 老师是精通python，若是有任何关于编程上的问题和学习上的问题 请随时跟老师沟通
课件：EC00GCPY02 试听课-模块代码切换-Python(中)(模块代码切换)(20190916)

学生自我介绍

两种学习方式：图形方式，不会涉及真正编写代码，可以锻炼逻辑能力
            代码方式，讲python语法，涉及真正编写代码，锻炼逻辑能力和代码编写能力，相对来说有些枯燥
'''

# 代码方式
'''
1. 画太阳花

2. 执行进度条

3. 一行代码

4. 看漫画

5. 'hello world'
'''
# 画太阳花
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    # print(pos())
    if abs(pos()) < 1:  #判断画笔是否回到起点
        break
end_fill()
done()

# # 执行进度条
# import time
#
# def bar(scale):
#     print('===========执行开始============')
#     for i in range(scale + 1):
#         a = '*' * i
#         b = '.' * (scale - i)
#         c = (i / scale) * 100
#         print('\r{:^3.0f}%[{}->{}]'.format(c, a, b), end = '')  #\r 表示将光标的位置回退到本行的开头位置
#         time.sleep(0.05)
#     print('\n===========执行结束============')
#
# bar(100)

# # 一行代码
# # 快速排序
# qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [ qs( [x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]] ) ] )[0]
# list1 = [1,6,9,8,2]
# print(qs(list1))
# 打印99乘法表
# print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))
# # 看漫画
# import antigravity

# # 'hello world'
# print('hello world')
# 课后
'''
用学生的账号发布作品和上传视频。（作品会通过微信公众号推送到家长微信）
试听课后在排课系统里填写“表单反馈”和“课程反馈”；“课程反馈”填写完成后转发到家长群
'''

student_name = input("请输入一个人的名字：")

print(student_name)

