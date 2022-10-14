import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y, x])

arr.sort()

for y, x in arr:
    print(x, y)