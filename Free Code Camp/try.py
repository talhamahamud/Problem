T=int(input())

for i in range(T):
    N, K=map(int, input().split())
    # X=int(input())
    inList= input().split()
    list1=[int(p) for p in inList]

    for j in range(N):
        if K-list1[i]>=0:
            print(1)
            K=K-i
        else:
            print(0)
    



        