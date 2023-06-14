list=[1, 2, 3, 4, 5]

def swapposition(list, pos1, pos2, pos3, pos4):

    list[pos1], list[pos2], list[pos3], list[pos4]=list[pos4], list[pos3], list[pos2], list[pos1]
    return list

pos1, pos2, pos3, pos4=0,1,3,4

print(list[::-1])
list.reverse()
print(list)
list.reverse()
print(swapposition(list, pos1, pos2, pos3, pos4))

print("the thing is very good")

