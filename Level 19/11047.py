import sys

N, K = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

cnt = 0

for i in arr[::-1]:    
    if(K // i == 0):
        continue
    
    cnt += K // i
    K = K - (i * (K // i))

    if(K == 0):
        break

print(cnt)