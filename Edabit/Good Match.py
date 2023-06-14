def goo_match(li):

    m = int(len(li)/2)
    if len(li) % 2 == 0:
        l1 = []
        for i in range(0, m):
            if i == 0:
                p = li[0]+li[1]
                l1.append(p)
            else:
                p = li[i*2]+li[i*2+1]
                l1.append(p)
        print(l1)
    else:
        print("bad match")

goo_match([5, 7, 9, -1])