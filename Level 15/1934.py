import sys

def lcm(a, b):
    while(b):
        a, b = b, a % b
    return a

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(int(a * b / lcm(a, b)))