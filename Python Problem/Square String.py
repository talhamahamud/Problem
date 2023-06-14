m = input("Pls input a word here: ")
d = []
for i in m:
    d.append(i)
l = sorted(d)
lenl = len(l)
d = lenl/2
summ = int(lenl)-int(d)
n = 0
pp = 0
if lenl % 2 == 0:
    for i in range(0, summ):
        n = n+2
        if l[n-2] == l[n-1]:
            pp += 2

        else:
            print("No")
            break
else:
    print("No")

if pp == len(l):
    print("Yes")
