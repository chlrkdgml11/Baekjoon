import sys

N = int(sys.stdin.readline().strip())

arr = []

for s in str(N):
    arr.append(s)

arr.sort(reverse=True)

for s in arr:
    print(s, end='')