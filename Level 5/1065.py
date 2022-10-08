def H(a):
    cnt = 0
    for i in range(1, a + 1):
        sum = 0
        if(i < 100):
            cnt += 1
        elif(i >= 100 and i < 1000):
            for j in str(i):
                sum += int(j)

            if(sum / 3 == i // 10 % 10):
                cnt += 1
    print(cnt)

H(int(input()))