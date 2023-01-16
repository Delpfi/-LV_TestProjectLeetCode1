import roman

S = roman.toRoman(1994)

charToNum = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
prev = 0
total = 0
Ss = S[::-1]
for numeral in Ss:
    cur = charToNum[numeral]


    if cur >= prev:
        total += cur
    else:
        total += -1 * cur
    prev = cur

print(total)