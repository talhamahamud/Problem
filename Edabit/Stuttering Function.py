def stuttering(word):
    m= word
    list1=[]
    for i in m:
        list1.append(i)

    li=list1[0]+list1[1]
    print(f"{li}... {li}... {word}")

stuttering("outstanding")