import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

pre_sum = []
sum = 0

for i in arr:
    sum += i
    pre_sum.append(sum)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    if(a == b):
        print(arr[a-1])
    elif(a == 1):
        print(pre_sum[b-1])
    else:
        print(pre_sum[b-1] - pre_sum[a-2])