N = int(input())

sum = 1

for i in range(0, 1000000000, 6):
    sum += i

    if(sum >= N):
        print((i // 6) + 1)
        break