def square_digits(number):
    str_num = str(number)
    list1=[]
    for i in str_num:
        list1.append(i)

    list2=[]
    for i in list1:
        list2.append(int(i)**2)
    
    string1=''
    for i in list2:
        string1= string1 + str(i)

    print(string1)
square_digits(3212)