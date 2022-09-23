n=int(input())
temp=n
n=abs(n)
r=0
while(n>0):
    s=n%10
    r=r*10+s
    n=n//10
if temp>0:
    print(r)
if temp<0:
    print(-(r))

    