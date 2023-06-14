def society_name(list1):

    lpl = sorted(list1)
    n = ""
    for i in lpl:
        n = n+i[0]
    print(n)

society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])