import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    dict = {}

    for _ in range(n):
        a, b = map(str, sys.stdin.readline().split())

        try:
            dict[b].append(a)
        
        except:
            dict[b] = [a]
            
    fact = 1

    for i in dict:
        fact = fact * (len(set(dict[i])) + 1)

    print(fact - 1)