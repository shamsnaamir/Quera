a = int(input())
b = int(input())
##
v = 0
c = a
while c!=0:
    g = c%10
    v = v*10+g
    c=int(c/10)
aa =v
##
v = 0
c = b
while c!=0:
    g = c%10
    v = v*10+g
    c=int(c/10)
bb =v
##
b =  str(b)
a = str(a)
if aa<bb:
    print(a+" < "+b)
elif aa>bb:
    print(b+" < "+a)
else:
    print(b+" = "+a)
