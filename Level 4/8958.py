import sys

for i in range(int(input())):
    test = sys.stdin.readline()
    score = 0
    accum = 1
    for t in test:
        if(t == 'O'):
            score += accum
            accum += 1
        else:
            accum = 1
    print(score)