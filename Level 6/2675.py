import sys

T = int(input())

arr = [0 for i in range(T)]

for i in range(T):
    arr[i] = sys.stdin.readline().split()
    arr[i][0] = int(arr[i][0])

for i in range(T):
    
    for j in range(len(arr[i][1])):

        for k in range(arr[i][0]):
            print(arr[i][1][j], end = '')
    print('')