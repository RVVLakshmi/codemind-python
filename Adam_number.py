n=int(input())
s=n*n
n=str(n)
m=n[::-1]
m=int(m)
k=m*m
s=str(s)
k=str(k)
if s==k[::-1]:
    print('True')
else:
    print('False')
