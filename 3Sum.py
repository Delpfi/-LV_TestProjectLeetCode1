#Сумма цифр в списке.


num = [-1,0,1,2,-1,-4]
num1 = sorted(num)
d = len(num1)
result = []

for i in range(d):
    j = i+1
    k = d-1
    while j<k:
        s = num1[i] + num1[j] + num1[k]
        if s>0:
            k -=1
        elif s<0:
            j += 1
        else:
            t = num1[i], num1[j], num1[k]
            j +=1
            t1 = sorted(t)
            if t1 in result:
                continue
            else:
                result.append(t1)
print(result)
if d<3:
    print("Список меньше 3-х цифр")
#return


"""
for i in range(d):
    for j in range(i+1,d):
        for k in range(j+1,d):
            if(num[i]+num[j]+num[k] ==0):
                t = num[i],num[j],num[k]
                t1 = sorted(t)
                if t1 in result:
                    continue
                else:
                    result.append(t1)
print(result)

"""




