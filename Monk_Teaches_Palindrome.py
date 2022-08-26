t=int(input())
for i in range(t):
    a=input()
    if a[::-1]!=a:
        print("NO")
    else:
        if len(a)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")