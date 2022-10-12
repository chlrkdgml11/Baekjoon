N = int(input())

cnt = 0

arr = list(map(int, input().split()))

for i in arr:
    if(i == 1):
        continue

    if(i == 2):
        cnt += 1
        continue
    
    for j in range(2, i):
        if(i % j == 0):
            break
        else:
            if(j == i - 1):
                cnt += 1

print(cnt)