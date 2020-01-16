z = []
for i in range(1,999999999999):
    x = int(input(""))
    if x == 0:
        break
    else:
        z.append(x)
z.reverse()
for t in z:
    print(t)
