import sys

while(1):
    arr = list(map(int, sys.stdin.readline().split()))

    if(arr[0] == 0 and arr[1] == 0 and arr[2] == 0):
        break

    arr.sort()

    if(arr[2] ** 2 == arr[0] ** 2 + arr[1] ** 2):
        print('right')
    else:
        print('wrong')