n=int(input())
l=list(map(int,input().split()))
for j in range(0,n):
    if l[j]%2==0:
        print(l[j],end=' ')
for i in range(0,n):
    if l[i]%2!=0:
        print(l[i],end=' ')