def series_resistance(list1):
    n=0
    for i in list1:
        n=n + i
    print(n)
    if n>=1:
        print(f"{n} ohms")

    else:
        print(f"{n} ohm")
    
series_resistance([1, 5, 6, 3])