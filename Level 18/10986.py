import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)+1):
        if(sum(arr[i:j]) % M == 0):
            cnt += 1

print(cnt)