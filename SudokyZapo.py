import copy
Res = []
def Perest(head, ForTail):
    """

    """


    if not ForTail:
        Res.append(head)
        return
    for c in ForTail:
        #head1 = copy.deepcopy(head)
        head1 = head[:]
        head1.append(c)
        Fortail1 = ForTail - {c}
        Perest(head1, Fortail1)
        pass
"""
set1 = {1,2,3}
Perest([], set1)
print(Res)
"""

class Solution:
    def solveSudoku(self, board):
        Len = len(board)
        self.Cyfry = set()
        for i in range (1,Len+1):
            self.Cyfry.add(str(i))
        self.BlkSz = 3

        Col = []
        for j in range (Len):
            Set1 = set()
            for i in range(Len):
                if board[i][j] != ".":
                    Set1.add(board[i][j])
            Col.append(Set1)
        Matr = copy.deepcopy(board)
        Res = self.BldRow(Matr,Col,0)


    def BldRow(self, Matr,Col,i):
        Matr1 = copy.deepcopy(Matr)
        Col1 = copy.deepcopy(Col)
        Cfr1 = set()
        Poz = []
        for cf,ind in zip(Matr1[i], range(len(Matr))):
            if cf ==".":
                Poz.append(ind)
            else:
                Cfr1.add(cf)
        Cfr2= self.Cyfry - Cfr1
        Vars = Perest([], Cfr2)
        for Var in Vars:
            bCol = True
            for ind, cf in zip (Poz, Var):
                if cf in Col1[ind]:
                    bCol=False
                    break
            if not bCol:
                continue
            for ind, cf in zip(Poz,Var):
                Matr1[i][ind] = cf
                Col1[ind].add(cf)
            bCol = BlkVer(Matr1,i)
            if not bCol: continue
            if i == len(Matr1) - 1:
                return Matr1
            Res = BldRow(Matr1,Col1, i+1)
            if Res:
                return Res
        return False


Matr = [
    ["1",".",".","3"],
    [".",".","4","."],
    ["2",".","1","."],
    ["3",".",".","1"]
]

a = Solution()
a.solveSudoku(Matr)