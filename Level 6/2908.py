arr = list(map(int, input().split()))

for i in range(2):
    arr[i] = arr[i] // 100 + arr[i] // 10 % 10 * 10 + arr[i] % 10 * 100

print(max(arr))