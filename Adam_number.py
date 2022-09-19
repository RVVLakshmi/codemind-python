n=input()
s=n[::-1]
n=int(n)
s=int(s)
g=n*n
h=s*s
l=str(h)
if str(g)==l[::-1]:
    print('True')
else:
    print('False')
