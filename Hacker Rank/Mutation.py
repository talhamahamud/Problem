def mutate_string(string, position, character):
    list_word=[]
    for i in string:
        list_word.append(i)
    list_word.pop(position)
    list_word.insert(position, character)
    print(position)
    print (list_word)
    word=''
    for i in list_word:
        word=word+i
    return word

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)