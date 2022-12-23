import sys

while(True):
    input = list(sys.stdin.readline().rstrip())

    if(input == ['.']):
        break

    arr = []

    for s in input:
        if(s == '(' or s == ')' or s == '[' or s == ']'):
            arr.append(s)
    
    result = []
    condition = True

    for i in range(len(arr)):
        if(arr[i] == '(' or arr[i] == '['):
            result.append(arr[i])
        
        else:
            if(arr[i] == ')'):
                try:
                    if(result[-1] != '('):
                        condition = False
                        break
                    
                    elif(result[-1] == '('):
                        del result[-1]

                except:
                    condition = False
                    break

            elif(arr[i] == ']'):
                try:
                    if(result[-1] != '['):
                        condition = False
                        break
                    
                    elif(result[-1] == '['):
                        del result[-1]

                except:
                    condition = False
                    break

    if(condition):
        print('yes')
    else:
        print('no')
