import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

sum, total = 0, 0

for i in arr:
    sum += i
    total += sum

print(total)