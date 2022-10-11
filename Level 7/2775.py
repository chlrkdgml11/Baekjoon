T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    f0 = [x for x in range(1, n+1)]

    for p in range(k):
        for q in range(1, n):
            f0[q] += f0[q-1]
    
    print(f0[-1])