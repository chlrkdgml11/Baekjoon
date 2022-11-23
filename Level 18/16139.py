import sys

S = sys.stdin.readline().rstrip()

q = int(sys.stdin.readline())

alpha = {}

for s in 'abcdefghijklmnopqrstuvwxyz':
    arr = []
    for i in range(len(S)):
        arr.append(S[:i+1].count(s))
    
    alpha[s] = arr

for _ in range(q):
    a, l, r = sys.stdin.readline().rstrip().split()
    l, r = int(l), int(r)

    if(l-1 < 0):
        x = 0
    else:
        x = alpha[a][l-1]

    print(alpha[a][r] - x)
