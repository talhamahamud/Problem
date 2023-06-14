inp1 = int(input('pls input length number of ypur list: '))
lst = []
for i in range(1, (inp1+1)):
    inpp2 = int(input(
        "pls input the numbers of the list and don't input numbers less then 10: "))
    if inpp2 >= 10:
        if str(inpp2) == str(inpp2)[::-1]:
            lst.append(inpp2)
        else:
            while True:
                inpp2 += 1
                if str(inpp2) == str(inpp2)[::-1]:
                    lst.append(inpp2)
                    break
    else:
        print("sorry, you don't input a valid number!!!")
print(f"Your palindrome list is {lst}")



