N = int(input())

Final = N
R = 0
L = 0
cnt = 0

while(1):
    R = Final % 10
    L = Final % 10 + Final // 10

    if(L >= 10):
        L = L % 10

    Final = R * 10 + L
    cnt += 1

    if(Final == N):
        break

print(cnt)