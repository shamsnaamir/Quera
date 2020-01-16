a = input().split()
k = int(a[2])
l = []
for j in range(k):
    l.append(input())
if(k%2==1):
    print("0")
else:
    if(k==int(a[0])*int(a[1])):
        print(-1)
    else:
         print(1)
         if(str(a[0])+" "+str(a[1]) in l):
             if(str(int(a[0])-1)+" "+str(int(a[1])-1) in l):
                 print(str(int(a[0])-1)+" "+str(int(a[1])))
             else:
                 print(str(int(a[0])-1)+" "+str(int(a[1])-1))
         else:
             print(str(a[0])+" "+str(a[1]))
