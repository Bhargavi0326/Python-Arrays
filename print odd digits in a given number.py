N=int(input())
mylist = []
while(N!=0):
    a = N % 10
    if a%2!=0:
        mylist.append(a)
    N = int(N/10)
if len(mylist)==0:
    print(-1)
else:
    print(*mylist[::-1])
