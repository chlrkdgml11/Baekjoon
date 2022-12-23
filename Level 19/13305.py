import sys

N = int(sys.stdin.readline())

roads = list(map(int, sys.stdin.readline().split()))

costs = list(map(int, sys.stdin.readline().split()))

result = 0

m = costs[0]

for i in range(N-1):
    if(costs[i] < m):
        m = costs[i]     
    result += m * roads[i]

print(result)