def fun1(value):
    n=0
    for i in value:
        n=n+1
    return n

def count_characters(list1):
    j=0
    for i in list1:
        j=j+fun1(i)
    
    print(j)

count_characters(["", ""])