import sys

N = int(sys.stdin.readline().strip())

arr = [0] * 10001

for i in range(N):
    arr[int(sys.stdin.readline().strip())] += 1

for x in range(10001):
    if(arr[x] != 0):
        for y in range(arr[x]):
            print(x)