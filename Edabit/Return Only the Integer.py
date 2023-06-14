def return_only_integer(list1):
    li = []
    for i in list1:
        if type(i) == int:
            li.append(i)
    print(li)

return_only_integer([9, 2, "space", "car", "lion", 16])