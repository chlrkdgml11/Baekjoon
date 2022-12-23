import sys

N = int(sys.stdin.readline())

for _ in range(N):
    input = sys.stdin.readline()

    arr = []
    result = True

    for i in range(len(input)):
        if(input[i] == '('):
            arr.append(input[i])
        
        elif(input[i] == ')'):
            if(len(arr) == 0):
                # print('NO')
                result = False
                break
            
            else:
                if(arr[-1] == '('):
                    del arr[-1]

                else:
                    # print('NO')
                    result = False
                    break
        # print(arr)

    if(result == False):
        print('NO')
        continue

    if(len(arr) != 0):
         print('NO')
    else:
        print('YES')
            