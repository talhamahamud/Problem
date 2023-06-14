l=[]
for i in range(1,1000):
    if i%3==0 or i%5==0:
        l.append(i)

n=0
for i in l:
    n=n+i

print (n)
