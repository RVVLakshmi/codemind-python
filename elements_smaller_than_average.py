n=int(input())
l=list(map(int,input().split()))
c=0
s=sum(l)//n
for i in range(0,n):
    if l[i]<=s:
       c+=1 
print(c)
