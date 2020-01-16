a,b,c,d = int(input()) , int(input()), int(input()), int(input())
jam = str(a+b+d+c)+".000000"
def ashar(x,zz):
    y = len(str(x)) - len(str(zz))
    if(y==0):
        x+=".000000"
    else:
        y-=1
        if(y>=0):
            x+="0"*(6-y)
    return x
main = (a+b+d+c)/4
main = ashar(str(main),int((a+b+d+c)//4))
z = a*b*c*d
z= ashar(str(z),int(z))
m1 = ashar(str(min(a,b,c,d)),min(a,b,c,d))
m2 = ashar(str(max(a,b,c,d)),int(max(a,b,c,d)))
print("Sum : "+jam)
print("Average : "+main)
print("Product : "+z)
print("MAX : "+m2)
print("MIN : "+m1)
