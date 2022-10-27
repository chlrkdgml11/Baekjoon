arr_1 = [4,7,9]

def binary_serch(arr, target):
    arr.sort()
    start = 0
    end = len(arr) - 1 

    while(start <= end):
        mid = (start + end) // 2

        if(arr[mid] == target):
            return mid
        
        elif(arr[mid] < target):
            start = mid + 1
        
        else:
            end = mid - 1
    
    return None

print(binary_serch(arr_1, 4))