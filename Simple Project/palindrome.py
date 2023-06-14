inputCheak = int(input("Pls input number's that you want to cheak: "))
for i in range(inputCheak):
    InputNumber = int(
        input("pls input a number that you want to cheak palindrome: "))
    if str(InputNumber) == str(InputNumber)[::-1]:
        print("It's a palindrome number")
    else:
        while True:
            InputNumber += 1    
            if str(InputNumber) == str(InputNumber)[::-1]:
                print(f"The next palindrome number is {InputNumber}")
                break
