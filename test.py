fibs = [1,1]
for i in range(50):
    if i == len(fibs):
        fibs.append(fibs[-1] + fibs[-2])

    print(fibs[i])