# G
import itertools
n = input().replace(' ','')
str1 = ''
for i in itertools.combinations(range(len(n)), 1):
    i = i[0]
    if n[i] != '0':
        str1 += n[i] * (i+1)
sum = 0
for i in set(itertools.permutations(str1,len(str1))):
    sum += int(''.join(i))
print(sum % (1000000000 + 7))

# for i in itertools.combinations(range(len(n)), 1):
#     print(i[0])
# for i in range(len(n)):
#     if n[i] != '0':
#         str1 += n[i] * (i+1)

# list1 = list(set([''.join(i) for i in list(itertools.permutations(str1,len(str1)))]))
# sum = 0
# for temp in list1:
#     sum += int(temp)
# print(sum % (1000000000 + 7))