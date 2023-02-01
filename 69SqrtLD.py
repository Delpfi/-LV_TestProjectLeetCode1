x = 3

r = x//2
l = 0
poo = 0
if x == 1:
    print(1)

while l<r:
    poo = (l+r)//2

    if poo*poo <= x:
        l = poo +1
    elif poo* poo > x:
        r = poo-1

print(r)








