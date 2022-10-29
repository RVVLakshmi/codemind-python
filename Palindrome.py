def pal(n):
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==s:
        print('True')
    else:
        print('False')
n=int(input())
s=n
pal(n)
        