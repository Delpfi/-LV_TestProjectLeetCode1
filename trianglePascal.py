n = 5

treangle = [[1]]
"""
for i in range(1,n):
    treangle.append([1] * (i+1))
    for j in range(1,i):
        treangle[i][j] = treangle[i-1][j]+ treangle[i-1][j-1]
print(treangle)
"""


for i in range(1,n):
    treangle.append([1]* (1+i))

for i in range(1,n):
    for j in range(1,i):
        treangle[i][j] = treangle[i-1][j] + treangle[i-1][j-1]
print(treangle)

"""
h=0
for i in treangle:
    h = 0
    while h<=n+1:
        for j,y in zip(i,range(n+1)):
            if j == 0:
                i.pop(y)
                h+=1
            else:
                h += 1
"""








#print(treangle)
"""
p = [1,2,4,0]
for y, k in zip(p,range(len(p))):
    if y == 0:
        p.pop(k)

"""








