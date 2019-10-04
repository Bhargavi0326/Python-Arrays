import math
S=input()
li=list(S)
Q=len(li)
if Q%2==0:
    n=Q//2
    li[n]='*'
    li[n-1]='*'
else:
    m=math.ceil(Q//2)
    li[m]='*'
print("".join(li))
        

