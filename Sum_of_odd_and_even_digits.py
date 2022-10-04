n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for k in range(0,n):
    if k%2==0:
        c+=l[k]
    else:
        s+=l[k]
if s-c==0:
    print('YES')
else:
    print('NO')
    