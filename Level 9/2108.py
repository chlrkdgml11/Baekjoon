import sys
from collections import Counter

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(round(sum(arr) / N))

print(arr[N // 2])


if(len(arr) == 1):
    print(Counter(arr).most_common()[0][0])
else:
    if(Counter(arr).most_common()[0][1] == Counter(arr).most_common()[1][1]):
        print(Counter(arr).most_common()[1][0])
    else:
        print(Counter(arr).most_common()[0][0])

print(max(arr) - min(arr))