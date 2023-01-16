s = "((]"
stack = []
dct =  {")" : "(", "]" : "[", "}" : "{"}
So = {"(" , "[", "{" }
Sz = { ")",  "]",  "}"}




for c in s:
    if c in So:
        stack.append(c)
    elif c in Sz:
        if len(stack) == 0:
            print(False)
        ch = dct.get(c)
        c1 = stack.pop()
        if ch != c1:
            print(False)



"""
if c in dct.keys():
    stack.append(c)
elif c in dct.values():
    print(k) 
"""


