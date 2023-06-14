def string(x):
    if type(x) == str :
        return True

def filter_list(list1):
    listStr=[]
    for i in list1:
        if string(i) != True:
            listStr.append(i)

    print(listStr)

filter_list([1, 2, "aasf", "1", "123", 123])
