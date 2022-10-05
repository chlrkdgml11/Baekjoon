X = int(input())
N = int(input())

arr = list()
sum = 0

for i in range(N):
    arr.append(list(map(int, input().split())))
    sum = sum + arr[i][0] * arr[i][1]

if(sum == X):
    print('Yes')
else:
    print('No')