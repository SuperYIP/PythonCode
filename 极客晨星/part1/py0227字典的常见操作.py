#coding=utf-8
'''
1. 修改字典元素
2. 删除元素
'''

    # 1. 修改字典元素
# info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '中国北京'}
# print(info)
# new_id = input("请输入新的学号：")
# info['id'] = int(new_id)
# print("修改后学号为：%s" % info['id'])
# print("修改后学号为：{1} {0}".format(info['id'], 300))
# print(info)
# new_id = input("请输入新的学号：")
# info['id'] = new_id
# print(info)

# info['salary'] = 200    # key不存在则在字典末尾加入键值对
# print(info)
    # 2. 删除元素
# del info['address'] # 删除单个元素
# info.clear()    # 清空字典内元素
# print(info)
# del info    # 删除整个字典
# print(info)

    # 课堂练习
lis = [["k", ["qwe", 20, {"k1": ["tt", 3, "1"]}, 89], "ab"]]
print(lis[0][1][2]['k1'][2])
lis[0][1][2]['k1'][2] = "101"
print(lis)