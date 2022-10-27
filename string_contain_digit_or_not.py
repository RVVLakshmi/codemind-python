import re
s=input()
t=len(re.findall('[0-9]',s))
if(t>0):
    print("Contains {} digit".format(t))
else:
    print("Doesn't contain digit")