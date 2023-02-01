# CombinationSum2_2.py


class Solution:
    def combinationSum2(self, candidates, target):
        """

        Args:
            candidates: List[int]
            target: int

        Returns:
            Res: List[List[int]]
        """
        self.Stack = 0
        # Будущий результат
        self.Res = []  # set()
        #  Цель
        self.target = target
        #  Отсеиваем тех кандидотв, кто больше цели,
        Cands1 = [x for x in candidates if x <= target]
        # Выясняем, есть ли кандидаты, равные цели
        Cnt = Cands1.count(target)
        # Если есть, добавляем один список в результат и
        # удаляем кандидатов, равных цели.
        if Cnt:
            #self.Res.add((target,))
            self.Res.append([target])
            self.Cands2 = [x for x in Cands1 if x < target]
        else:
            self.Cands2 = Cands1
        # Сортируем омтавшихся кандидатов в порядке убывания
        self.Cands2.sort(reverse=True)
        #  Каждому кандидату приписывам величину self.Sm[i],
        #  равную сумме его и всех последующих до конца списка (по убыванию)
        Len = len(self.Cands2)
        self.Sm = [0 for i in range(Len)]
        i = Len-1
        Sm1 = 0
        while i >= 0:
            Sm1 += self.Cands2[i]
            self.Sm[i] = Sm1
            i -= 1
        # --- закончили с self.Sm
        #  Каждому кандидату приписывам величину self.Next[i],
        #  которая содержит индекс ближайшего следующего элемента
        #  списка, отличного от этого.
        #  То есть, например, self.Cands2 = [10, 6, 6, 5, 4, 4, 4, 3]
        #  Тогда self.Next = [1, 3, 3, 4, 7, 7, 7, 8]
        #  Последний, как видно, указывает за конец списка, то есть равен Len.
        #  А если элемент не повторяется, то просто self.Next[i] == i+1  .
        self.Next = [0 for i in range(Len)]
        Curr = -1
        Neq = Len
        i = Len - 1
        while i >= 0:
            if self.Cands2[i] != Curr:
                Curr = self.Cands2[i]
                self.Next[i] = i+1
                Neq = i+1
            else:
                self.Next[i] = Neq
            i -= 1
        # --- закончили с self.Next


        self.Len = Len
        # Для всех кандидатов вызываем self.FindSumFrom
        # Эта функция ищет подходящие суммы для всех кандидатов, начиная
        # с себя и дальше по списку
        # Функция добавляет комбинации в self.Res
        # Причем добавляет комбинации не в виде списков, а в виде кортежей
        # Это связано с тем, что self.Res - множество, а элементами множества
        # могут быть кортежи, но не списки
        # Потом мы преобразуем это множество кортежей в список списков,
        # как это требуется.
        # Функция возвращает код возврата (см. строку документации к функции).
        #
        #for i in range(Len):
        #            Code = self.FindSumFrom(i, [], 0)

        #Code = self.FindSumFrom(0, [], 0)
        #"""
        # Переьираем стартовые позиции, от которых считаем суммы
        i = 0
        while i < self.Len:
            Code = self.FindSumFrom(i, [], 0)
            if Code == "m":
                i += 1
                continue
            elif Code == "s":
                break
            elif Code == "e":
                i = self.Next[i]
                continue
            elif Code == "f":
                i += 1
                continue
        #"""
        #for i in range(Len):
        #    Code = self.FindSumFrom(i, [], 0)
        #    if Code == "finish":
        #        break

        ResPreSet = [tuple(x) for x in self.Res]
        Set1 = set(ResPreSet)
        Res1 = [list(x) for x in Set1]
        ###### преобразуем множество кортежей в список списков
        #LstRes = [list(x) for x in self.Res]
        #return LstRes
        return Res1
    # --------------------------------------------------------------
    def FindSumFrom(self, i0, Head, SmHead):
        """
        Ищем подходящие суммы для кандидатов, начиная i0-го

        Возвращает код.
        Этот код принимает следующие значения
        "m" (more) - i0-й кандидат оказался слишком велик
        "s" (smaller) - i0-й кандидат оказался слишком
            мал вместе со всем своим хвостом
        "e" (equel) - i0-й кандидат как раз дополнил SmHead до target
        "f" (full)- полностью исчерпали все варианты, связанные с хвостом
        Args:
            i0: int - индекс, с какого элемента списка начинаем
            Head: list[int] - голова списка-предполагаемого результата:
               элементы self.Cands2, уже включенные в предполагаемый результат.
            SmHead: int - сумма, уже накопленная к моменту вызова.
                 i0-й элемент сюда не входит

        Returns:

        """
        self.Stack += 1
        # Если даже прибавиви все последующие, не доберём до цели
        # - то конец этой ветки.
        if SmHead + self.Sm[i0] < self.target:
            self.Stack -= 1
            return "s"
        # Если прибавление всей суммы звоста как раз и даёт target,
        # то зафиксируем этот результат - и конец этой ветки.
        if SmHead + self.Sm[i0] == self.target:
            self.Res.append(Head + self.Cands2[i0:])
            self.Stack -= 1
            return "s"
        # Проверяем, а не все ли до конца списка - одинаковые элементы
        # Если да, то можно просто решить.
        # Уже  ясно, что сумма хвоста больше, чем target
        # Иначе сработала бы проверка выше (одна из).
        # Если из этих элементов можно сложить недостающий остаток суммы,
        # то это делаем, и дальше (до конца хвоста) делать нечего
        # А если нельзя - то тем более делать нечего.
        Lst = self.Cands2[i0:]
        Set1 = set(Lst)
        if len(Set1) ==  1:
            x = Lst[0]
            y = self.target-SmHead  # Сколько ещё не хватает
            (k, m) = divmod(y, x)
            if m == 0:  # делится без остатка
                n = y // x
                Res1 = [x] * n
                self.Res.append(Head + Res1)
                self.Stack -= 1
                return "s"

        # Сумма головы списка, включая и i0-й элемент
        NewSmHead = SmHead + self.Cands2[i0]
        # Если это слишком много - закончим
        # Если дальше добавлять в список, то будет ещё больше
        # Поэтому конец.этой ветви.
        if NewSmHead > self.target:
            self.Stack -= 1
            return "m"

        # Новая голова списка - добавили i0-й элемен
        NewHead = Head + [self.Cands2[i0]]
        # Если как раз цель - включили в результат
        # И продолжать нет смысла: если что-то прибавлять,
        # то будет уже больше цели.
        if NewSmHead == self.target:
            #self.Res.add(tuple(NewHead))
            self.Res.append(NewHead)
            self.Stack -= 1
            return "e"
        # Значит ещё меньше цели
        # Пытаемся продолжить список дальше
        #for i in range(i0+1, self.Len):
        i = i0 + 1
        while i < self.Len:
            Code = self.FindSumFrom( i, NewHead, NewSmHead)
            if Code == "m":
                #i += 1
                i = self.Next[i]
                continue
            elif Code == "s":
                #self.Stack -= 1
                #return "f"
                break
            elif Code == "e":
                i = self.Next[i]
                continue
            elif Code == "f":
                i += 1
                continue

        self.Stack -= 1
        return "f"





a = Solution()
candidates = [10,1,6,2,7,6,6,2, 1,5, 1,1,1,1,1,1,1,1,1]
#candidates = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#candidates = [4,2,1,1]
target = 3  #
#target = 8
Res = a.combinationSum2(candidates, target)
print(Res)
