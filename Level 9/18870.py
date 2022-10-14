import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i]:i for i in range(len(arr2))}

for x in arr:
    print(dic[x], end = ' ')