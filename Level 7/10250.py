import sys

T = int(input())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    floor = N % H
    room = (N // H) + 1

    if(N % H == 0):
        floor = H
        room = N // H

    print(floor * 100 + room)