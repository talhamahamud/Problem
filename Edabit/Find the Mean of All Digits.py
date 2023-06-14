def mean(num):
    m=str(num)
    h=[]
    for i in m:
        h.append(i)
    y=len(h)

    n=0
    for i in m:
        n=n+int(i)
    print(n/y)
    
mean(33)