import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    for i in range(1, min(a, b) + 1):
        if(a % i == 0 and b % i == 0):
            max = i
    return max

for i in range(1, N):
    print(arr[0] // gcd(arr[0], arr[i]), '/', arr[i] // gcd(arr[0], arr[i]), sep = '')