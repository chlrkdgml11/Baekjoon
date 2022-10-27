import sys

N, M = map(int, sys.stdin.readline().split())

dict_1 = {}

for _ in range(N):
    input = sys.stdin.readline().strip()
    dict_1[input] = 1

arr = []

for _ in range(M):
    input = sys.stdin.readline().strip()
    try:
        dict_1[input] += 1
        arr.append(input)
    except:
        dict_1[input] = 1

arr.sort()

print(len(arr))
for s in arr:
    print(s)
