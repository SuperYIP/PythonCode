#coding=utf-8
'''
课件
setheading():设置箭头朝向
十九关和二十关较难
'''

# 第十九关
'''
    每次画E的时候，都需要将初始坐标调整到E这个字母的左上角那个点，如果E的方向发生了转动，
则找的点也要相应转动，总之，找的点是E字母正常朝向的左上角的点。
    但是这样找起来是比较麻烦的，毕竟有那么多的E，角度也是各种各样的。但是如果每次将坐标调整到
E的左上角而无论E的朝向是怎样的，那么就方便多了。这其实是隐藏着规律的。
    当箭头朝向上面的时候，即heading=90，我们发现将E绝对左上角的点的y-length就是E的相对左上角的点
    当箭头朝向左面的时候，即heading=180，我们发现将E绝对左上角的点的y-length,x+length就是E的相对左上角的点
    当箭头朝向下面的时候，即heading=270，我们发现将E绝对左上角的点的x+length就是E的相对左上角的点
    当箭头朝向右面的时候，即heading=0，不需额外操作
'''

# 第二十关
'''
    每一行的y是不变的，每一行的x是有规律的，找x规律画
'''

from turtle import *
def q(sides,length,Acolor):
    color(Acolor)
    begin_fill()
    for i in range(0, sides):
        forward(length)
        right(360/sides)
    end_fill()
q(4,400,(255,0,0))

done()
