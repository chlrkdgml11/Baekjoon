a = int(input())
A = list(map(int, str(a))) 

b = int(input())
B = list(map(int, str(b))) 

c = [0, 0, 0]

for i in range(3):
    c[i] = a * B[2-i]
    print(c[i])

print(c[2] * 100 + c[1] * 10 + c[0])