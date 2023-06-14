def list_operation(x, y, n):
    li=[]
    for i in range(x, y+1):
        if i%n==0:
            li.append(i)
    print(li)

list_operation(15, 20, 7)