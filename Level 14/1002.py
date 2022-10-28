import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    r = r1 + r2

    if(dis == 0 and r1 == r2):
        print(-1)
    elif(abs(r1-r2) == dis or r == dis):
        print(1)
    elif(abs(r1-r2) < dis < r):
        print(2)
    else:
        print(0)