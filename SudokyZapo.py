# Sudoku1.py
import copy

# Res = []
"""
set1 = {1,2,3}
Perest([], set1)
print(Res)
"""


class Solution():
    def solvesudoku(self, board):
        Len = len(board)
        self.Cyfry = set()
        for i in range(1, Len + 1):
            self.Cyfry.add(str(i))
        self.BlkSz = 2
        #
        Col = []
        for j in range(Len):
            Set1 = set()
            for i in range(Len):
                if board[i][j] != ".":
                    Set1.add(board[i][j])
            Col.append(Set1)
        Matr = copy.deepcopy(board)
        Res = self.BldRow(Matr, Col, 0)
        for i in range(Len):
            for j in range(Len):
                board[i][j] = Res[i][j]

    def BldRow(self, Matr, Col, i):
        """
        Заполняем одну строку в матрице.
        Args:
            Matr: матрица, заполненная до i-й строка, не включая её.
            Col:
            i: номер строки, которую нужно заполнить.
               Номер, начиная с нуля.

        Returns:

        """
        Matr1 = copy.deepcopy(Matr)
        Col1 = copy.deepcopy(Col)
        Cfr1 = set()
        Poz = []
        # Выясняем, какие символы уже есть в строке и в каких позициях
        for cf, ind in zip(Matr1[i], range(len(Matr))):
            if cf == ".":
                Poz.append(ind)
            else:
                Cfr1.add(cf)
        #
        Cfr2 = self.Cyfry - Cfr1
        Vars = self.Perest(Cfr2)
        for Var in Vars:
            bCol = True
            for ind, cf in zip(Poz, Var):
                if cf in Col1[ind]:
                    bCol = False
                    break
            if not bCol:
                continue
            for ind, cf in zip(Poz, Var):
                Matr1[i][ind] = cf
                Col1[ind].add(cf)
            bCol = self.BlkVer(Matr1, i)
            if not bCol:
                continue
            if i == len(Matr1) - 1:
                return Matr1
            Res = self.BldRow(Matr1, Col1, i + 1)
            if Res:
                return Res
        return False

    def BlkVer(self, Matr1, i):
        #if i == 0 :
        #    return True
        k = self.BlkSz
        if (i+1) % k != 0:
            return True
        Len = len(Matr1)
        i0 = i - k + 1
        i1 = i
        for j1 in range(k-1,Len,k):
            j0 = j1-k +1
            bb = self.Blk1Ver( Matr1,i0,i1,j0,j1)
            if not bb:
                return False
        return True

    def Blk1Ver(self, Matr1,i0,i1,j0,j1):
        Set1 = set()
        for i in range(i0,i1+1):
            for j in range(j0,j1+1):
                Set1.add(Matr1[i][j])
        M = len(Set1)
        M1 = self.BlkSz**2
        return M == M1


    def Perest(self, SourSet):
        """

        """

        def Perest1(head, ForTail):
            if not ForTail:
                Res.append(head)
                return
            for c in ForTail:
                # head1 = copy.deepcopy(head)
                head1 = head[:]
                head1.append(c)
                Fortail1 = ForTail - {c}
                Perest1(head1, Fortail1)

        Res = []
        Perest1([], SourSet)
        return Res


Matr = [["1", "2", "3", "."],
        [".", ".", "1", "2"],
        ["2", "1", ".", "."],
        ["4", ".", "2", "."]
        ]

a = Solution()
a.solvesudoku(Matr)
for row in Matr:
    print(row)