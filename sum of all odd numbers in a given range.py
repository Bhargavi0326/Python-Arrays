def oddSumRange(n):
    interval=(n+1)//2
    sum=interval*interval
    return sum
def sumRange(l,r):
    return oddSumRange(r)-oddSumRange(l-1)
l,r=map(int,input().split())
print (sumRange(l,r))
