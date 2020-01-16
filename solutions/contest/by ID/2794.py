a= input()
a = a.split(" ")
b= input()
b = b.split(" ")
c= input()
c = c.split(" ")
def iss(x,aa):
    t =0
    if x in a[aa]:
        t+=1
    if x in b[aa]:
        t+=1
    if x in c[aa]:
        t+=1
    return t
if (iss(a[0],0)==1):
    x = a[0]
if (iss(b[0],0)==1):
    x = b[0]
if (iss(c[0],0)==1):
    x = c[0]  
if (iss(a[1],1)==1):
    y = a[1]
if (iss(b[1],1)==1):
    y = b[1]
if (iss(c[1],1)==1):
    y = c[1]
print(str(x)+" "+str(y))
