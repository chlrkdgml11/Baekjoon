def d():
    nature = list(range(1, 10001))
    generator = []

    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        generator.append(i)
    
    for k in generator:
        if k in nature:
            nature.remove(k)

    for n in nature:
        print(n)

d()