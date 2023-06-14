def swap_case(s):
    list_of_str = []
    for i in s:
        list_of_str.append(i)
    new_list = []
    n = 0
    for i in list_of_str:
        if i == i.upper():
            new_list.insert(n, i.lower())

        elif i == i.lower():
            new_list.insert(n, i.upper())
        n = n+1

    sentence = ''
    for i in new_list:
        sentence = sentence+i

    return sentence


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
