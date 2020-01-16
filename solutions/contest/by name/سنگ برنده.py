n = int(input())
a= False
for j in range(1000):
    if(n==1):
        a =True
        break
    if(n%2==0):
        n/=2
    else:
        n=3*n
        n+=3
if(a):
    print("Yes")
else:
    print("No")
