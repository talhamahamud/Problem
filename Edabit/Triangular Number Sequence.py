def Triangular(p):
    if p==1:
        print(1)
    else:
        n=1
        list1=[]
        for i in range(2, p+2):
            n=n+i
            list1.append(n)
            # print(n)
        del list1[-1]
        # print(list1)
        print(list1[-1])

p=int(input("pls input:"))
Triangular(p)