# Sudoku1.py
import copy
#Res = []
"""
set1 = {1,2,3}
Perest([], set1)
print(Res)
"""

class Solution():
    def solvesudoku(self, board):
        Len = len(board)
        self.Cyfry = set()
        for i in range(1, Len+1):
            self.Cyfry.add(str(i))
        self.BlkSz = 3
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
        #
        for i in range(Len):
            for j in range(Len):
                board[i][j] = Res[i][j]



    def BldRow(self, Matr, Col, i):
        """
        Заполняем одну строку в матрице и рекурсивно - все нижележащие.

        .
        Args:
            Matr: матрица, заполненная до i-й строка, не включая её.
            Col: список множеств. Их столько, сколько столбцов.
                Каждое множесьво соответствует одному столбцу (по порядку).
                Множество содержит символы, которые на данный момент
                присутствуют в столбце. (То есть при данном заполнении Matr)
            i: номер строки, которую нужно заполнить.
               Номер, начиная с нуля.
        Returns:
            1) Список списков - правильно заполненну матрицу, если это удалось.
            2) False - если не удалось.
        """
        Matr1 = copy.deepcopy(Matr)
        Col1 = copy.deepcopy(Col)
        # Выясняем:
        Cfr1 = set() # какие символы уже есть в строке
        Poz = [] # какие позиыии пока не заняты
        for cf,ind in zip(Matr1[i], range(len(Matr1))):
            if cf ==".":
                Poz.append(ind)
            else:
                Cfr1.add(cf)
        # Какими символами можно заполнять пустые места (их ещё нет в строке)
        Cfr2 = self.Cyfry - Cfr1
        # Все возможные перестановки этих символов.
        # То есть вариант заполнения пустых позиций в строке.
        # (список списков. Один вариант - один список)
        Vars = self.Perest(Cfr2)
        # Перебираем все варианты перестановок по одному.
        Col2 = copy.deepcopy(Col1)
        for Var in Vars:
            # Проверяем, нет ли повторов в столбцах
            Col1 =Col2
            bCol = True
            for ind, cf in zip (Poz, Var):
                if cf in Col1[ind]:
                    bCol=False
                    break
            if not bCol:
                continue
            # Если по стобцам всё в порялке
            Col2 = copy.deepcopy(Col1)
            for ind, cf in zip(Poz,Var):
                # заполняем пустые места в строке
                Matr1[i][ind] = cf
                # Записываем, что в таких-то столбцах появились новые элементы
                Col1[ind].add(cf)
            # Проверяем на ниличие повторов в блоках
            bBlk = self.BlkVer(Matr1,i)
            if not bBlk:
                continue
            # Если это была последняя строка - всё в порядке
            if i == len(Matr1) - 1:
                return Matr1
            # А не последняя - заполняем следующкю строку и все ниже неё
            Res = self.BldRow(Matr1,Col1, i+1)
            # Если вернулась какая-то матрица (а не False) - это результат
            if Res:
                return Res
        # А иначе - пока неудача.
        return False
    # -----------------------------------------------
    def BlkVer(self, Matr1,i):
        #if i == 0:
        #    return True
        k = self.BlkSz
        if (i+1) % k != 0:
            return True
        Len = len(Matr1)

        i0 = i - k + 1
        i1 = i
        for j1 in range(k-1, Len, k):
            j0 = j1 - k + 1
            bb = self.Blk1Ver(Matr1, i0, i1, j0, j1)
            if not bb:
                return False
        return True
    # -----------------------------------------------
    def Blk1Ver(self, Matr1, i0, i1, j0, j1) :
        #return True
        Set1 = set()
        for i in range(i0, i1+1):
            for j in range(j0, j1+1):
                Set1.add(Matr1[i][j])
        M = len(Set1)
        M1 = self.BlkSz**2
        return M == M1


    def Perest(self, SourSet):
        """

        """


        Res = []
        self.Perest1([], SourSet, Res)
        return Res

    def Perest1(self, head, ForTail, Res):
        # def Perest1(head, ForTail):
        #    nonlocal Res
        if not ForTail:
            Res.append(head)
            return
        for c in ForTail:
            # head1 = copy.deepcopy(head)
            head1 = head[:]
            head1.append(c)
            Fortail1 = ForTail - {c}
            self.Perest1( head1, Fortail1, Res)


Matr = [ ["1",".", ".", "."],
         [".", ".", ".", "."],
         [".", "1", ".", "."],
         [".", ".", ".","."]
    ]
"""
Matr = [ ["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
"""
"""
Matr = [ ["1", "2", "3", "4"],
         ["3", "4", "1", "2"],
         ["2", "1", "4", "3"],
         ["4", "3", "2","1"]
    ]

"""
"""
Matr = [ ["1",".", ".", "."],
         [".", ".", ".", "."],
         [".", ".", ".", "."],
         [".", ".", ".", "."]

    ]
"""

a =  Solution()
#print(Solution.__dict__)
#exit()
a.solvesudoku(Matr)
for row in Matr:
    print(row)

"""
['1', '4', '3', '2']
['2', '3', '4', '1']
['4', '1', '2', '3']
['3', '2', '1', '4']

"""