import sys

arr = [i for i in range(1, 31)]

for _ in range(28):
    n = int(sys.stdin.readline())

    arr.remove(n)

for i in arr:
    print(i)