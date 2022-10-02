s=input()
k='aeiou'
g=0
for i in range(0,len(k)):
    if k[i] not in s:
        g+=1
        print(k[i],end=' ')
if g==0:
    print('0')
    