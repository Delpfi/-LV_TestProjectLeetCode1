# CombinationSum2.py

class Solution:
    def combinationSum2(self, candidates, target):
        """

        Args:
            candidates: List[int]
            target: int

        Returns:
            Res: List[List[int]]
        """
        # Будущий результат
        self.Res =  set() #[]
        #  Цель
        self.target = target
        #  Отсеиваем тех кандидотв, кто больше цели,
        Cands1 = [x for x in candidates if x <= target]
        # Выясняем, есть ли кандидаты, равные цели
        Cnt = Cands1.count(target)
        # Если есть, добавляем один список в результат и
        # удаляем кандидатов, равных цели.
        if Cnt:
            self.Res.add((target,))
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
        # --- закончили с self.Sm[i]
        self.Len = Len
        # Для всех кандидатов вызываем self.FindSumFrom
        # Эта функция ищет подходящие суммы для всех кандидатов, начиная
        # с себя и дальше по списку
        # Функция ничего не возвращает, а добавляет комбинации в self.Res
        # Причем добавляет комьинации не в виде списков, а в виде кортежей
        # Это связано с тем, что self.Res - множество, а элементами множества
        # могут быть кортежи, но не списки
        # Потом мы преобразуем это множество кортежей в список списков,
        # как это требуется.
        for i in range(Len):
            self.FindSumFrom(i, [], 0)
        # преобразуем множество кортежей в список списков
        LstRes = [list(x) for x in self.Res]
        return LstRes
    # --------------------------------------------------------------
    def FindSumFrom(self, i0, Head, SmHead):
        """
        Ищем подходящие суммы для кандидатов, начиная i0-го

        Args:
            i0: int - индекс, с какого элемента списка начинаем
            Head: list[int] - голова списка-предполагаемого результата:
               элементы self.Cands2, уже включенные в предполагаемый результат.
            SmHead: int - сумма, уже накопленная к моменту вызова.
                 i0-й элемент сюда не входит

        Returns:

        """
        # Сумма головы списка, включая и i0-й элемент
        NewSmHead = SmHead + self.Cands2[i0]
        # Если это слишком много - закончим
        # Если дальше добавлять в список, то будет ещё больше
        # Поэтому конец.этой ветви.
        if NewSmHead > self.target:
            return
        # Гсли даже прибавиви все последующие не доберём до цели
        # - тоже конец
        if SmHead + self.Sm[i0] < self.target:
            return
        # НОвая голова списка - добавили 0-й элемен
        NewHead = Head + [self.Cands2[i0]]
        # Если как раз цель - включили в результат
        # И продолжать нет смысла: если что-то прибавлять,
        # то будет уже больше цели.
        if NewSmHead == self.target:
            self.Res.add(tuple(NewHead))
            return
        # Значит ещё меньше цели
        # Пытаемся продолжить список дальше
        for i in range(i0+1, self.Len):
            self.FindSumFrom( i, NewHead, NewSmHead)






a = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
Res = a.combinationSum2(candidates, target)
print(Res)