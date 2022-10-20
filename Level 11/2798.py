import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

sum = min(arr) * 3

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = arr[i] + arr[j] + arr[k]
            if(temp <= M and temp >= sum):
                sum = temp

print(sum)