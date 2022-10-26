import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    rank = 1
    for j in range(N):
        if(i == j):
            continue
        
        if(arr[i][0] < arr[j][0]):
            if(arr[i][1] < arr[j][1]):
                rank += 1
    print(rank, end = ' ')