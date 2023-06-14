def amplify(n):
    l = []
    for i in range(1, n+1):
        if i % 4 == 0:
            l.append(i*10)
        else:
            l.append(i)

    print(l)
    
amplify(25)