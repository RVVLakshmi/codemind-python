def Ami(m,n):
    s=0
    k=0
    for i in range(1,m,1):
        if m%i==0:
            s+=i
    for j in range(1,n,1):
        if n%j==0:
            k+=j 
    if s==n and k==m:
        print('Amicable')
    else:
        print('Not Amicable')
m=int(input())
n=int(input())
Ami(m,n)
        
            