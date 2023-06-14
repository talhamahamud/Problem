import random


def trueFunction(number):
    table = []
    n = 0
    for i in range(1, 11):
        n = n+number
        table.append(n)
    return table


def RohanFunction(number):
    table = []
    n = 0
    for i in range(1, 11):
        n = n+number
        table.append(n)
    c = random.randint(0, 9)
    table[c] = table[c]+random.randint(1, 2)
    return table


def funcCheck(table, number):
    for i in range(1, 11):
        if table[i-1] != (i*number):
            return (i-1)


if __name__ == '__main__':
    number = int(input("pls enter your table's first number: "))
    rohan = RohanFunction(number)
    print(f"This is rohan table {rohan}")
    check = funcCheck(rohan, number)
    print(f"The problem of Rohan function is in this index: {check}")
    print(f"True table is: {trueFunction(number)}")
