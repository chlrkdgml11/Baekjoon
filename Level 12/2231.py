import sys

N = int(sys.stdin.readline())

arr = []

for i in range(1, 1000001):
    sum = i
    for s in range(len(str(i))):
        sum += int(str(i)[s])
    arr.append(sum)

try:
    print(arr.index(N) + 1)
except:
    print(0)
