n=int(input())
t=n
l=len(str(n))
s=0
while(n!=0):
    r=n%10
    s+=r**l
    l=l-1
    n=n//10
if s==t:
    print('True')
else:
    print('False')
