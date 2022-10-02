n=int(input())
l=list(map(int,input().split()))
m=int(input())
a=l.index(m)
s=0
for i in range(0,a+1):
    s+=l[i]
print(s)