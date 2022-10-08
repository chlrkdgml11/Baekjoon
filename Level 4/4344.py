import sys

N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

sum = 0
avg = 0

for i in range(N):
    for j in range(1, len(arr[i])):
        sum += arr[i][j]
    avg = sum / arr[i][0]
    
    cnt = 0
    for k in range(arr[i][0]):
        if(avg < arr[i][k+1]):
            cnt += 1
    result = round(cnt / arr[i][0] * 100, 3)
    print('%.3f'%result, end = '')
    print('%')
    sum = 0