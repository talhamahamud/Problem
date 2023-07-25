T=int(input())
for i in range(T):
    N=int(input())
    om_0 = input()
    addy_0 = input()
    
    om_1=om_0.split('0')
    addy_1=addy_0.split('0')

    om=sorted(om_1, key=len)
    addy=sorted(addy_1, key=len)
    if len(om[::-1][0]) > len(addy[::-1][0]):
        print('Om')
    elif len(om[::-1][0]) == len(addy[::-1][0]):
        print('Om')
    else:
        print('Addy')

    