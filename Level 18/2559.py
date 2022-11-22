import sys

N, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

result = []
result.append(sum(arr[:K]))

for i in range(N - K):
    result.append(result[i] - arr[i] + arr[i+K])

print(max(result))