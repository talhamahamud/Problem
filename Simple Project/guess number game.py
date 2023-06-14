import random
ls1 = [i for i in range(4, 13)]
rChoice = int(random.choice(ls1))
print("now we playing for player 1")
i = 0
while True:
    i = i + 1
    pChoice = input('pls guessa number btween "4" and "13": ')
    if int(pChoice) > rChoice:
        print("you enter a greater number, pls enter a small number")
    elif int(pChoice) < rChoice:
        print("you enter a small number pls enter a greater number")
    else:
        print(f'you successfully guess the number and that is {pChoice}')
        break


ls2 = [i for i in range(4, 13)]
lChoice = int(random.choice(ls2))
print(f"now we playing for player 2 ")
p = 0
while True:
    p = p+1
    pChoice = input('pls guessa number btween "4" and "13": ')
    if int(pChoice) > lChoice:
        print("you enter a greater number, pls enter a small number")
    elif int(pChoice) < lChoice:
        print("you enter a small number pls enter a greater number")
    else:
        print(f'you successfully guess the number and that is {pChoice}')
        break

if i > p:
    print("player 2 is the winner")
else:
    print("player 1 is the winner")
