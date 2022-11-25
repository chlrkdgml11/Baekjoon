import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

result = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    sum = 0
    for j in range(N):
        if(i == 0 and j == 0):
            result[i][j] = arr[i][j]
            sum = arr[i][j]
        else:
            result[i][j] = arr[i-1][j] + sum
            sum = result[i][j]

print(result)