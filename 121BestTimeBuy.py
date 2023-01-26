Lst = [5,5,4,9,3,8,5,5,1,6,8,3,4]
Len0 = len(Lst)
SumMax = 0
d=0
SumMax1 = 0
"""
for i in prices:
    d +=1
    for y in prices[d:]:
        if y < i:
            continue
        elif y>i:
            SumMax1 = y-i
            SumMax= max(SumMax,SumMax1)
            

print("SumMax=",SumMax)

r=1
while d < Len0:
    left = prices[d]
    right = prices[r]

    if right == Len0+1:
        d +=1
    if right< left :
        r += 1
        continue
    elif  right>left:
        SumMax1 = right - left
        SumMax = max(SumMax, SumMax1)
"""

x = Lst[0]
OptMax= x
OptMin = x
MinLeft = x
OptDif = 0
for Curr in Lst[1:]:
    if Curr - MinLeft > OptDif :
        OptMax = Curr
        OptMin = MinLeft
        OptDif = OptMax-OptMin
        continue
    if Curr < OptMax and Curr >OptMin:
        continue
    if Curr > OptMax:
        OptMax = Curr
        if MinLeft < OptMin:
            OptMin = MinLeft
        OptDif= OptMax - OptMin
        continue

    if Curr < OptMin  and Curr < MinLeft:
        MinLeft = Curr
        continue

print(OptDif)



