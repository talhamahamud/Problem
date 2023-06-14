def add_time(inp, inp1):
        f1=inp.split(' ')#for inp
        f2=f1[0].split(':')#for inp
        list_time=map(int, f2)#for f2
        int_time=list(list_time)#for list_time

        s1=inp1.split(':')#for inp1
        s1_int=map(int, s1)#for s1
        s1_list = list(s1_int)#for s1

        print(f1)
        print(int_time)
        print(s1_list)

        
add_time('4:12 AM', '3:12')

