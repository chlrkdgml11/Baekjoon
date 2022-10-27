import sys
import sys

N, M = map(int, sys.stdin.readline().split())

arr_1 = []

for _ in range(N):
    arr_1.append(sys.stdin.readline().strip())

arr_2 = []

for _ in range(M):
    arr_2.append(sys.stdin.readline().strip())

cnt = 0

for s in arr_2:
    if(s in arr_1):
        cnt += 1

print(cnt)