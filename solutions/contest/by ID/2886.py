v = input()
v = v.split(" ")
a = int(v[0])
b = int(v[1])
a-=12
b -= 60
if(a<0):
    a = 0-a
if(b<0):
    b = 0-b
if(a>=12):
    a-=12
if(b>=60):
    b-=60

a = str(a)
b = str(b)
if(len(a)==1):
    a="0"+a
if(len(b)==1):
    b = "0"+b
print(a+":"+b)
