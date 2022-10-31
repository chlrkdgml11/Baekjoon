import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while(b):
        a, b = b, a % b
    
    return a

print(gcd(a, b))

print(int(a * b / gcd(a, b)))