a = int(input())

b = int(input())

arr = []

def primenumber(x):
    if(x == 1):
        return False
    elif(x == 2):
        return x
    else:
        for i in range(2, x):
            if(x % i == 0):
                return False
        return x

for x in range(a, b+1):
    if(primenumber(x)):
        arr.append(x)

if(arr):
    print(sum(arr))
    print(min(arr))
else:
    print(-1)