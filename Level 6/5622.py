S = input()

arr = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

sum = 0

for i in range(8):
    for j in str(S):
        if(j in arr[i]):
            sum = sum + i + 3

print(sum)