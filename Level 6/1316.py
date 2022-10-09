N = int(input())

arr = []
arr_set = []

for i in range(N):
    arr.append(input())
    arr_set.append(set(arr[i]))
    arr_set[i] = list(arr_set[i])

cnt = 0

for i in range(N):
    tester = 0
    for j in arr_set[i]:
        count = arr[i].count(j)
        
        test = j

        for k in range(count - 1):
            test += j

        if test in arr[i]:
            tester += 1
    if(tester == len(arr_set[i])):
        cnt += 1

print(cnt)