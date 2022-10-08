string = []

for i in range(97, 123):
    string.append(chr(i))

S = input()

for i in string:
    if(i in S):
        print(S.index(i), end = ' ')
    else:
        print('-1', end = ' ')