import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(list(map(str, sys.stdin.readline().split())))
    arr[i][0] = int(arr[i][0])

arr.sort(key = lambda x:x[0])

for x, y in arr:
    print(x, y)