a,b,c=map(int,input().split())
g=0
for i in range(a,b+1,1):
    if i%c==0:
        g+=1
print(g)        