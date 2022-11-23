from itertools import combinations

arr = [1, 2, 3, 4, 3]

com_arr = list(combinations(arr, 2))

print(com_arr[0])

print(sum(com_arr[0]))