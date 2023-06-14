def get_first_value(x):
    for i in x:
        if i.isdigit() :
            print("not found")
        else:
            print(i)

get_first_value([1,2,3,"s",4])