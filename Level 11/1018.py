from re import L
import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().strip())

board_W = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
board_B = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

W = 'WBWBWBWB'
B = 'BWBWBWBW'

for i in range(N-7):
    for j in range(M-7):
        if(arr[i][j] == 'W'):
            





