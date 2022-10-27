import sys

N = int(sys.stdin.readline())
arr_1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr_2 = list(map(int, sys.stdin.readline().split()))

arr_1.sort()

def binary_search(arr, target, start, end):
    while(start <= end):
        mid = (start + end) // 2

        if(arr[mid] == target):
            return mid
        
        elif(arr[mid] > target):
            end = mid - 1

        else:
            start = mid + 1

    return None

for i in arr_2:
    if(binary_search(arr_1, i, 0, N-1) is not None):
        print(1, end = ' ')
    else:
        print(0, end = ' ')