import sys

def primenumber(x):
    if(x == 1):
        return False

    for i in range(2, int(x**0.5)+1):
        if(x % i == 0):
            return False
    return True

arr = []

for i in range(2, 123456 * 2 + 1):
    if(primenumber(i)):
        arr.append(i)

while(1):
    a = int(sys.stdin.readline())

    if(a == 0):
        break

    cnt = 0

    for i in arr:
        if(i > a and i <= a * 2):
            cnt += 1

    print(cnt)