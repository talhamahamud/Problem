def abcmath(a, b, c):
    list1=[a*2]
    for i in range(b-1):
        list1.append(list1[i]*2)

    if list1[::-1][0]%c==0:
        print(True)
    else:
        print(False)

abcmath(1, 2, 3)