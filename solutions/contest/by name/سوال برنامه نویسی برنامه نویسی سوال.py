x=int(input())
y = input()
listo = y.split(" ")
listo.reverse()
stri = ''
c = 1
for i in listo:
    stri +=i
    if c!=x:
        stri+=" "
print(stri)
