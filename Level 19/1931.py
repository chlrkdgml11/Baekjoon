import sys

N = int(sys.stdin.readline())

time = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    time.append([a, b])

time.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end = time[0][1]

for i in range(1, N):
    if(end <= time[i][0]):
        cnt += 1
        end = time[i][1]

print(cnt)
