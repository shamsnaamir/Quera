count = int(input(""))
names = []
kl = 0
counter = 0
for counter in range(0,count):
    z = input("")
    names.append(z)
    counter = (counter + 1)
bg = 0
for bg in range(0,count):
    names[bg] = set(names[bg])
    counter = (counter-1)
    bg = (bg+1)
fty = 0
for fty in range(0,count):
    names[fty] = len(names[fty])
names.sort()
assert names[(count-1)] < 20
print(names[(count-1)])
