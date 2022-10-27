import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))

dict_1 = {}

dict_2 = {}

for i in A:
    try:
        dict_1[i] += 1
    except:
        dict_1[i] = 1

for j in B:
    try:
        dict_1[j] += 1
    except:
        dict_1[j] = 1

cnt = 0

for k in dict_1:
    if(dict_1[k] == 1):
        cnt += 1

print(cnt)