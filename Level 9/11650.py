import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()

for s in arr:
    print(s[0], s[1], sep=' ')