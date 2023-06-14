def next_in_line(list1, x):
    list1.remove(list1[0])
    list1.append(x)
    print(list1)

next_in_line([5, 6, 7, 8, 9], 1)