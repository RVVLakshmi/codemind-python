n=int(input())
s=str(n*n)
n=str(n)
if s.endswith(n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
