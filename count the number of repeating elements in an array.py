N=int(input())
li=[int(m) for m in input().split()]

if N<=100000:
    Q=1
    for i in li:
        if li.count(i)==2:
            Q+=1
            print(Q,end=' ')
    print()
    
        
        
