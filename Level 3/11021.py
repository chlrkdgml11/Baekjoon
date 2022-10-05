import sys

T = int(sys.stdin.readline())

arr = []

for i in range(T):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(T):
    print('Case #',end = '')
    print(i + 1, end = '')
    print(':', sum(arr[i]))