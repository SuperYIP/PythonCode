# coding=utf-8
def isNum(str):
    try:
        str = eval(str)
        if type(str) == type(10) or type(str) == type(1.0) or type(str) == type(1 + 1j):
            return True
        else:
            return False
    except:
        return False


f = isNum('123')
print(f)
