class Solution:
    def __init__(self):
        self.Res = []
        self.N = 0
    def Gen(self, Str, n1, n2):
        if n2>n1:
            return
        if n1>self.N//2:
            return
        if n1+n2 == self.N:
            self.Res.append(Str)
        self.Gen(Str + '(', n1+1, n2)
        self.Gen(Str + ')', n1, n2+1)

    def start(self, n):
        self.N =2*n
        self.Gen('(',1,0)
        return self.Res

a = Solution()
Res1 = a.start(2)
print(Res1)