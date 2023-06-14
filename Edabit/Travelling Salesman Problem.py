def possible_paths(num):
    n=1
    for i in range(1, num+1):
        n=n*i
    print(n)

possible_paths(9)

