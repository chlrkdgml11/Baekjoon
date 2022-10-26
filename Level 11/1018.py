import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().strip())

board_W = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
board_B = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

temp = 999

for i in range(N-7):
    for j in range(M-7):
        diff_1 = 0
        diff_2 = 0

        for a in range(8):
            for b in range(8):
                if(arr[i+a][j+b] != board_B[a][b]):
                    diff_1 += 1

                if(arr[i+a][j+b] != board_W[a][b]):
                    diff_2 += 1

        if(min(diff_1, diff_2) <= temp):
            temp = min(diff_1, diff_2)
        
print(temp)