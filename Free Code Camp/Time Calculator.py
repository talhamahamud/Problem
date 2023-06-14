def add_time(gTime, dT, day=''):
    list1 = gTime.split(":")
    ap = list1[1].split(" ")

    sumT = int(list1[0]) + (int((ap[0]))/60)
    print(sumT)

# add_time("5:30 PM")