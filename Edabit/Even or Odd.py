def Even_Odd(number):
    n=0
    for i in number:
        n=n+i

    if n%2 == 0:
        print("Even")
    else:
        print("Odd")

print(Even_Odd([1, 2, 1]))
