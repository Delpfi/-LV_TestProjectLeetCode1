nums = [1,2,3,1,4,5,6,7,8,9,8,46,6,4,4,4,4,4,4,1,5,3,2,1,46,7,9,101,101,10]

Sum = []
Sum1 = []
d = len(nums)
"""
for i in nums:
    if i not in Sum:
        Sum.append(i)
    else:
        Sum.remove(i)
print(Sum[0])
"""
Sett = set(nums)
SetL = len(Sett)
k = 0
Sum =[[i,0] for i in Sett]

for i in Sum:
    for j in nums:
        if i[0] == j:
            i[1]+=1

for i in Sum:
    if i[1] == 1:
        Sum1.append(i[0])



print(Sum1[0])








