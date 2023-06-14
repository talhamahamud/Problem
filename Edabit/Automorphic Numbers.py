def Automorphic_Numbers(n):
    sn=str(n)
    ln=[]
    for i in sn:
        ln.append(str(i))
    uln=ln[::-1]
    l=[]
    k=n**2
    h=str(k)
    j=''
    for i in h:
        l.append(str(i))
    ul=l[::-1]
    d=1 
    for i in range(len(sn)):
        if ul[i] == uln[i]:
            d=d*1
        else:
            d=d*0
    if d==1:
        print(True)
    else:
        print(False)

Automorphic_Numbers(76)
