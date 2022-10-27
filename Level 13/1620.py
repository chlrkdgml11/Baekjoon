import sys

N, M = map(int, sys.stdin.readline().split())

dict_1 = {}

for i in range(1, N + 1):
    input = sys.stdin.readline().strip()
    dict_1[i] = input
    dict_1[input] = i

for _ in range(M):
    question = sys.stdin.readline().strip()
    try:
        print(dict_1[int(question)])
    except:
        print(dict_1[question])