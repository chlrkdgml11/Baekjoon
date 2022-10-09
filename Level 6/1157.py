N = input()

N = N.upper()

element = list(set(N))
element_count = [0 for i in range(len(element))]

for i in range(len(element)):
    for j in range(len(N)):
        if(element[i] == N[j]):
            element_count[i] += 1

if(element_count.count(max(element_count)) >= 2):
    print('?')
else:
    print(element[element_count.index(max(element_count))])