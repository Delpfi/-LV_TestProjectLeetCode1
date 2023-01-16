#Самая длинная полидром. строка

s = 'babad'
n = len(s)
St = []
k = 0
Str = ''

x0 =0
y0 = 0
Len = 1
for i in range(0, n-1):
    for j in range(i+1, n):
        x= i
        y = j
        bPal = True
        while x<y:
            if s[x] != s[y]:
                bPal = False
                break
            x +=1
            y -=1
        if bPal:
            Len1 = j-i+1
            if Len1 > Len:
                x0 = i
                y0 = j
                Len = Len1
print(x0,y0,s[x0:y0+1])



"""
for x in range(0,n):
    if (len(S) <= 2):
        Str += S[0]
    for j in range(x+1,n):
        S1 = S[x]
        S2 = S[j]
        if(S1 == S2):
            s1 = S[x: j + 1]
            St.append(s1)


for i in St:
    Ss = i[::-1]
    if(Ss == i and len(i)>=k):
        k = len(i)
        Str = i

print(Str)


"""






