def u(s):
    d=0
    for x in s:
        if x.isdigit()==True:
           z=int(x)
           d=d+z
        
    return d
s=input()
print(u(s))