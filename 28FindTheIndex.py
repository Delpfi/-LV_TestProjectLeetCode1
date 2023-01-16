def FindStr(haystack,needle):
    k =0
    n = len(haystack)
    for x in range(0,n):
        for j in range(x,n):
            St = haystack[x:j+1]
            if St == needle:
                return x

    return -1




haystack = "sadbutsad"
needle = "sad"
a = FindStr(haystack,needle)
print(a)