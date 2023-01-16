Num = {'0':'_', '1':'*' , '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
digits = "58"
Arr =['']
d =1

if not digits:
    print(Arr)


for i in digits:
    k = Num[i]
    d *= len(k)
    Arr = [i+j for j in k for i in Arr]


print(sorted(Arr))



"""
if d<=4 and d>0:
    h = [h for h in Arr[0]]
    print(h)

else:

    h1 = [h+d for h in Arr[0] for d in Arr[1]]
    print(h1)
    
"""
