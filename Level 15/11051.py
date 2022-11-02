import sys
import math

N, K = map(int, sys.stdin.readline().split())

result = math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

print(result % 10007)