t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    if a==b:
        print('Lose')
    else:
        r=n//a
        y=b 
        while y<=n:
            if y%a==0:
                r-=1 
            y+=b 
        if r>=k:
            print('Win')
        else:
            print('Lose')