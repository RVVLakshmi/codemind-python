s=input()
p=input()
j=0
for i in range(0,len(s)):
    if s[i]==p:
        j=1
        print('True')
        print(i)
        break
if j==0:
    print('False')
        