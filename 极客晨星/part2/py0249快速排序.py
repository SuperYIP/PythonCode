# coding=utf-8
'''
课件
'''

def quickSort(list1, low, high):
    if low >= high:
        return list1
    # 记录排序序列的起始和结束位置
    start = low
    end = high
    base = list1[low]
    while low < high:   # 快速排序的结束条件
        while low < high and list1[high] >= base:
            high -= 1
        list1[low] = list1[high]
        while low < high and list1[low] < base:
            low += 1
        list1[high] = list1[low]
    # 循环结束，low=high，将基准元素放入正确位置
    list1[low] = base
    quickSort(list1, start, low-1)
    quickSort(list1, high+1, end)

lists=[30,24,5,58,18,36,12,42,39]
print(lists)
quickSort(lists, 0, len(lists)-1)
print(lists)
