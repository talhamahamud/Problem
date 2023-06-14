def card(list1):
    d = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0,
         9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
    n = 0
    for i in list1:
        n = n+d[i]

    print(n)

print("Tal mahamud in class room")
card([5, 9, 10, 3, "J", "A", 4, 8, 5])