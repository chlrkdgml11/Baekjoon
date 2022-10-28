import sys

K = int(sys.stdin.readline())

arr = []

arr_x = []

arr_y = []

for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())

    arr.append(b)

    if(a == 1 or a == 2):
        arr_x.append(b)
    elif(a == 3 or a == 4):
        arr_y.append(b)

w_idx = arr.index(max(arr_x))
h_idx = arr.index(max(arr_y))

space = max(arr_x) * max(arr_y)

empty_space_x = abs(arr[w_idx - 1] - arr[(w_idx + 1) % 6])
empty_space_y = abs(arr[h_idx - 1] - arr[(h_idx + 1) % 6])

print(K * (space - empty_space_x * empty_space_y))