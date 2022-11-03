import sys
import math

N = math.factorial(int(sys.stdin.readline()))

cnt = 0

for i in range(len(str(N)) - 1, -1, -1):
    if(str(N)[i] == '0'):
        cnt += 1

    else:
        break

print(cnt)