if __name__ == '__main__':
    s = input()
    string=[]
    for i in s:
        string.append(i)
    
    list1=[]
    for i in string:
        if i.isalnum()==True:
            list1.append('True')
        else:
            list1.append('False')
    if 'True' in list1:
        print('True')
    elif 'True' not in list1:
        print('False')
    list2=[]
    for i in string:
        if i.isalpha()==True:
            list2.append('True')
        else:
            list2.append('False')
    if 'True' in list2:
        print('True')
    elif 'True' not in list2:
        print('False')


    list3=[]
    for i in string:
        if i.isdigit()==True:
            list3.append('True')
        else:
            list3.append('False')
    if 'True' in list3:
        print('True')
    elif 'True' not in list3:
        print('False')

    list4=[]
    for i in string:
        if i.islower()==True:
            list4.append('True')
        else:
            list4.append('False')
    if 'True' in list4:
        print('True')
    elif 'True' not in list4:
        print('False')

    list5=[]
    for i in string:
        if i.isupper()==True:
            list5.append('True')
        else:
            list5.append('False')
    if 'True' in list5:
        print('True')
    elif 'True' not in list5:
        print('False')

