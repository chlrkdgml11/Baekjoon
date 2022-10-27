import sys

N = int(sys.stdin.readline())

dict_1 = {}

arr_1 = list(map(int, sys.stdin.readline().split()))

for i in arr_1:
    try:
        dict_1[i] += 1
    except:
        dict_1[i] = 1

M = int(sys.stdin.readline())

arr_2 = list(map(int, sys.stdin.readline().split()))

for j in arr_2:
    try:
        print(dict_1[j], end = ' ')
    except:
        print(0, end = ' ')