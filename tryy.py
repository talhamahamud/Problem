for _ in range(int(input())):
    a=int(input())
    p=list(map(int, input().split()))
    s=list(map(int, input().split()))
    
    om_count=0
    om_streak=om_count
    addy_count=0
    addy_streak=addy_count
    for i in range(a):
        if p[i]!=0:
            om_count+=1
        else:
            om_count=0

        if s[i]!=0:
            addy_count+=1
        else:
            addy_count=0
        om_streak=max(om_streak, om_count)
        addy_streak=max(addy_streak, addy_count)
    if om_streak>addy_streak:
        print('Om')
    elif om_streak<addy_streak:
        print('Addy')
    else:
        print('Draw')