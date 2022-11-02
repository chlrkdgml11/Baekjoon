import sys
import math

N, K = map(int, sys.stdin.readline().split())

fac = 1

for i in range(K):
    fac *= N
    N -= 1

print(int(fac / math.factorial(K)))

