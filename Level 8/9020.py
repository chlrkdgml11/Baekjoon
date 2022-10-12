def primenumber(x):
    if(x == 1):
        return False
    for i in range(2, int(x**0.5)+1):
        if(x % i ==0):
            return False
    return True

for _ in range(int(input())):
    n = int(input())

    a, b = n // 2, n // 2

    while(a > 0):
        if(primenumber(a) and primenumber(b)):
            print(a, b)
            break
        else:
            a -= 1
            b += 1