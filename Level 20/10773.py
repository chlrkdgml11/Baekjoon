import sys

K = int(sys.stdin.readline())

arr = []

for _ in range(K):
    input = int(sys.stdin.readline())

    if(input == 0):
        del arr[-1]

    else:
        arr.append(input)

print(sum(arr))