import sys

S = sys.stdin.readline().strip()

arr = []

l = len(S)

for i in range(l):
    for j in range(l):
        if(len(S[j:j+i+1]) != i + 1):
            continue
        arr.append(S[j:j+i+1])

print(len(set(arr)))