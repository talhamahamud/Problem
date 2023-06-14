def Missing(li):
    f_li ={1,2,3,4,5,6,7,8,9,10}
    li.sort()
    p= f_li- set(li)
    print(list(p)[0])

Missing([10, 5, 1, 2, 4, 6, 8, 3, 9])