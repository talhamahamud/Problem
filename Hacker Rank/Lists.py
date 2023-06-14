if __name__ == '__main__':
    empty_list = []
    N = int(input())
    functions = []
    n = -1

    for i in range(N):
        inp = input().split(' ')
        functions.append(inp)
        n = n+1

 
        if functions[n][0]=='insert':
            empty_list.insert(int(functions[n][1]), int(functions[n][2]))
        
        elif functions[n][0]=='print':
            print(empty_list)
        elif functions[n][0]=='remove':
            empty_list.remove(int(functions[n][1]))
        
        elif functions[n][0]=='append':
            empty_list.append(int(functions[n][1]))
        elif functions[n][0]=='sort':
            empty_list.sort()
        elif functions[n][0]=='pop':
            empty_list.pop()
        elif functions[n][0]=='reverse':
            empty_list.reverse()