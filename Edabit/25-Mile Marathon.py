def marathon(list1):
    n=0
    for i in list1:
        n=n+i
    if n==25:
        print(True)
    elif n*(-1)== abs(n):
        print(True)
        print(n*(-1))
    else:
        print(False)
marathon([25])