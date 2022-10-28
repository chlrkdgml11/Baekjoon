import sys

arr_x = []

arr_y = []

for i in range(3):
    a, b = map(int, sys.stdin.readline().split())
    arr_x.append(a)
    arr_y.append(b)

for j in range(3):
    if(arr_x.count(arr_x[j]) == 1): 
        x = arr_x[j]
    
    if(arr_y.count(arr_y[j]) == 1):
        y = arr_y[j]

print(x ,y)