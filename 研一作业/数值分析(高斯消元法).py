# coding=utf-8

a = [[1, 1, 1], [12, -3, 3], [-18, 3, -1]]
b = [6, 15, -15]
n = 2
k = 0
##消元过程
if a[k][k] == 0:
    print("停机")
else:
    while (k != n):
        for i in range(k + 1, n + 1):
            temp = a[i][k] / a[k][k]
            b[i] = b[i] - temp * b[k]
            for j in range(k, n + 1):
                a[i][j] = a[i][j] - temp * a[k][j]
        k = k + 1
## 回代过程
    if a[n][n] == 0:
        print("停机2")
    else:
        b[n] = b[n] / a[n][n]
        for k in range(n - 1, -1, -1):
            temp = 0
            for w in range(k , n):
                temp = temp + a[k][w + 1] * b[w + 1]
            b[k] = (b[k] - temp) / a[k][k]
        print(b)
