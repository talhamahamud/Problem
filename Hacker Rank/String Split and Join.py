def split_and_join(line):
    split_text=line.split(" ")
    join_func="-".join(split_text)
    
    return join_func
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)