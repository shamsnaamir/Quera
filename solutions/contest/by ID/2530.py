a = input()
n=0
for j in a:
    if(j=="T" or j=="D" or j=="L" or j=="F"):
        n+=1
print(2**n)
