def clone(list1):
  list2=[]
  for i in list1:
    list2.append(i)

  list1.append(list2)
  print(list1)

clone(["x", "y"])