mylist=[]
N= int(input())
while(N!=0):
    a=N%10
    mylist.append(a**2)
    N = int(N/10)
print(sum(mylist))
