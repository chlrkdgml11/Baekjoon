croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

N = input()

for i in croatia:
    N = N.replace(i, '*')

print(len(N))