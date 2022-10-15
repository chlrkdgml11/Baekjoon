import sys

N = int(sys.stdin.readline())

arr = [0, 1]

for i in range(2, N+1):
    arr.append(arr[i-1] + arr[i-2])

if(N == 0):
    print(0)
else:
    print(max(arr))