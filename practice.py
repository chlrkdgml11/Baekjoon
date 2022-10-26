import sys

W = 'WBWBWBWB'
B = 'BWBWBWBW'

board_01 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
board_02 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

N, M = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().strip())
print('')
print(arr[0][:8] == W)

