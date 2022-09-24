m=int(input())
n=int(input())
s=0
d=0
for i in range(1,m,1):
    if m%i==0:
        s+=i
for j in range(1,n,1):
    if n%j==0:
        d+=j
if s==n and d==m:
    print('Amicable')
else:
    print('Not Amicable')
    
        
        