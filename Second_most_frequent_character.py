str=input()
a=[0]*256
m=0
s=0
i=0
for i in range(len(str)):
    if str[i]!='':
        n=ord(str[i])
        a[n]+=1
for i in range(256):
    if a[i]>a[m]:
        s=m
        m=i
    elif a[i]>a[s] and a[i]!=a[m]:
        s=i
if((s)>m):
    print((chr)(s))
else:
    print("-1")