A, B = map(int, input().split())
C = int(input())

if(B + C >= 60):
    A = A + (B + C) // 60
    B = (B + C) % 60
else:
    B = B + C

if(A > 23):
    A = A - 24

print(A, B)