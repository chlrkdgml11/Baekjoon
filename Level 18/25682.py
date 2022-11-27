import sys

N, M, K = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

board_W = []
board_B = []
arr_W = ''
arr_B = ''
for x in range(K):
    if(x % 2 == 0):
        arr_W += 'W'
        arr_B += 'B'
    else:
        arr_W += 'B'
        arr_B += 'W'

for y in range(K):
    if(y % 2 == 0):
        board_B.append(arr_B)
        board_W.append(arr_W)
    else:
        board_B.append(arr_W)
        board_W.append(arr_B)

temp = 999

for i in range(N-K+1):
    for j in range(M-K+1):
        diff_1 = 0
        diff_2 = 0

        for a in range(K):
            for b in range(K):
                if(arr[i+a][j+b] != board_B[a][b]):
                    diff_1 += 1

                if(arr[i+a][j+b] != board_W[a][b]):
                    diff_2 += 1

        if(min(diff_1, diff_2) <= temp):
            temp = min(diff_1, diff_2)
        
print(temp)
