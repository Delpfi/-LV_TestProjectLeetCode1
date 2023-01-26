
"""
s = "Hello World"
s1 ="Today is a nice day"
a = s.split()
len1 = 0
for i in a:
    l = len(i)
    len1 = l

digits = [4,3,2,1]
s = ''
for i in digits:
    s += str(i)
s1 = int(s) + 1
s2 =[]
#s2 = [int(a) for a in str(s1)]
for a in str(s1):
    s2.append(int(a))
print(s2)

"""


def rec(n):
    if n == 2:
        return n
    if n == 1:
        return n
    return rec(n - 1) + rec(n - 2)

n = 4
res = rec(n)
print (res)