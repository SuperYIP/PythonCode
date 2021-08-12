# coding=utf-8
'''
课件
'''

# 递归实现
# def binarySearch(alist, data):
#     n = len(alist)
#     if n < 1:
#         return False
#     mid = n // 2
#     if alist[mid] > data:
#         return binarySearch(alist[0:mid], data)
#     elif alist[mid] < data:
#         return binarySearch(alist[mid+1:], data)
#     else:
#         return '{}在列表中位置为{}'.format(data,mid)

# 非递归实现
# def binarySearch(alist, data):
#     n = len(alist)
#     first = 0
#     last = n - 1
#     while first <= last:
#         mid = (last + first) // 2
#         if alist[mid] > data:
#             last = mid - 1
#         elif alist[mid] < data:
#             first = mid + 1
#         else:
#             return '{}在列表中位置为{}'.format(data,mid)
#     return False

# lis = [2, 4, 5, 12, 14, 23]
# print(binarySearch(lis, 4))
