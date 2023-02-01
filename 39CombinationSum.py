# CombinationSum.py

class Solution:
    def combinationSum(self, candidates, target):
        """

        Args:
            candidates:  List[int]
            target:  int

        Returns: List[List[int]]

        """
        """
        Идея такая.
        К каждому кандидату мы припишем ещё несколько кандидатов, кратных ему.
        Как можно больше, но так, чтобы больший из них был не больше аргета.
        Например, таргут=10, а есть кандидаты 2,3 и 7.
        Тогда к 2 мы припишем ещё 4, 6, 8, 10.
        А к 3 припишем 6 и 9.
        То есть кандидатов теперь будет 3 можества: {2,4,6,8 10}, {3,6,9}, {7}.
        Разбиение на множества имеет смысл: мы не можем складывать 2 и 8, 
        так это просто производные от 2.
        Таким образом, подбирая подходящие слагаемые, мы не можем брать больше 
        дного элемента из каждого множества.
        Кандидатов отсортируем по убыванию. 
        Параллельно сэтим (основным) списком будет несколько вспомогательных, 
        синхронизированных по индексу.
        В одном параллельном списке будет стоять число - значение числа из  
        candidates, которому кратен данный.
        В другом параллельном списке будет небольшой "список кратности". 
        Например, если данный элемент равен 15 и получен трёхкратным использованием 
        числа 5 (из candidates), то это будет [5,5,5]
        """
        self.Res = []  # set()
        #  Цель
        self.target = target
        #  Отсеиваем тех кандидотв, кто больше цели,
        Cands1 = [x for x in candidates if x <= target]
        # Выясняем, есть ли кандидат, равный цели
        try:
            Ind = Cands1.index(target)
            self.Res.append([target])
            del Cands1[Ind]
        except ValueError:
            pass
        # Создаём расширенный список кандидатов
        # В нём присутствуют и сами (исходные) кандидаты и их кратные
        # повторения
        # Например, если кандидат = 2, а цель = 7,
        # то в Cands1a попадут [2], [2,2], [2,2,2] - то есть не больше
        # цели в сумме.
        # Каждый элемент Cands1a - кортеж.
        # Он имеет структуру (x, Val, Lst),
        # где x:int - исходный кандидат Val:int - значение, кратное x,
        # Lst:List[int] - список с кратным повторением.исходного кандидата.
        # Например, (2, 6, [2,2,2])
        # Для каждого исходного кандидата создаём столько элементов Cands1a,
        # сколько раз его кратные "впмсываются" в цель. .
        Cands1a = []
        for x in Cands1:
            k = target // x
            Val = 0
            Lst = []
            for m in range(k):
                Val += x
                Lst.append(x)
                Cands1a.append((x, Val, Lst[:]))
        # Сортируем по убыванию.
        Cands1a.sort(key=lambda y: y[1], reverse=True)
        # Раскидываем Cands1a на 3 параллельных списка.
        self.Cands2 = []
        self.LstVal = []
        self.SetCnd = []
        for Tpl in Cands1a:
            (x, Val, Lst) = Tpl
            self.Cands2.append(Val)  # Например, 6
            self.LstVal.append(Lst[:])  # Например, [2,2,2]
            self.SetCnd.append(x)  # Например, 2.
        # Находим максимальные суммы хвостовых элементов,
        # включая текущий
        # А также список тех, кто в эти суммы входит.
        Len = len(self.Cands2)
        DctMax = {}
        # будущие суммы хвостовых элементов, включая текущий
        self.Sm = [0] * Len
        # Ьудущие множества элементов, образующих хвостовые суммы,
        # включая текущий
        self.SetSm = [set()] * Len  #
        self.LstSm = [[]] * Len  # LstVal-ы элементов, образовавших Sm

        for Ind in reversed(range(Len)):
            SetInd = self.SetCnd[Ind]
            DctMax[SetInd] = Ind

            Sm1 = 0
            Set1 = set()
            Lst1 = []
            for k in DctMax.keys():
                Ind1 = DctMax[k]
                Sm1 += self.Cands2[Ind1]
                Set1.add(self.SetCnd[Ind1])
                #Lst1.append(self.LstVal[k])
                Lst1 += self.LstVal[Ind1]
            self.Sm[Ind] = Sm1
            self.SetSm[Ind] = Set1.copy()
            self.LstSm[Ind] = Lst1[:]

        self.Stack = 0

        # Переьираем стартовые позиции, от которых считаем суммы
        self.Len = len(self.Cands2)
        i = 0
        while i < self.Len:
            Code = self.FindSumFromSt(i, [], 0, set())
            if Code == "n":
                i += 1
                continue
            elif Code == "s":
                break

        ResPreSet = [tuple(x) for x in self.Res]
        Set1 = set(ResPreSet)
        Res1 = [list(x) for x in Set1]
        ###### преобразуем множество кортежей в список списков
        # LstRes = [list(x) for x in self.Res]
        # return LstRes
        return Res1

    def FindSumFromSt(self, i0, Head, SmHead, StHead):
        """
        Ищем подходящие суммы для кандидатов, начиная i0-го

        Возвращает код.
        Функцмя заканчивает раьоту, когда:
        1) Все  потомки (какие имело сиысл) данного i0 (включая
        его в чистом виде) уже перебраны, и с этим кандидатом
        уже делать нечего.
        Вызывающей функции нужно брать следующий кандидат того же
        уровня, что и i0.
        2) Не только потомки этого (i0) кандидата уже бесперспективны,
        но и потомки того, что на этаж выше бесперспективны.
        Например, хвост уже недостаточен, чтобы достичь target.
        Тогда, если мы возьмём следующее i0 (а соответствующий
        кандидат не больше данного), то там тем более не хватит.
        Значит код може принимать 2 значения:
        1) "n" (next)
        2) "s" (stop).
        Этот код принимает следующие значения
        #"m" (more) - i0-й кандидат оказался слишком велик
        "n" (next) - i0-й кандидат
            1) оказался слишком велик
            2) как раз дополнил SmHead до target (без участия хвоста)
            3) все потомки ш0 перебрані
            Во всех случаях вызывающей функции нужно брать следующий
            кандидат.
        #"s" (smaller) - i0-й кандидат оказался
        "s" (stop) - i0-й кандидат оказался
            1) слишком мал вместе со своим максимальным хвостом
            2) равен target в сумме со своим максимальным хвостом.
            В обоих случаях дальше нет смысла наращивать Head.
            С єтим i0 уже ничего не сделаешь. Вызывающая функция должна
            откатить последний элемент Head и идти дальше.


        Args:
            i0: int - индекс, с какого элемента списка начинаем
            Head: list[int] - голова списка-предполагаемого результата:
               элементы self.Cands2, уже включенные в предполагаемый результат.
            SmHead: int - сумма, уже накопленная к моменту вызова.
                 i0-й элемент сюда не входит
            StHead: set - множество кандидатов, уже участвующих в Head (возможно,
                       в какой-то кратности).
        Returns:
        """
        if self.SetCnd[i0] in StHead:
            return "n"
        self.Stack += 1
        # Если даже прибавиви все последующие, не доберём до цели
        # - то конец этой ветки.
        if SmHead + self.Sm[i0] < self.target:
            self.Stack -= 1
            return "s"
        # Если прибавление всей суммы звоста как раз и даёт target,
        # то зафиксируем этот результат - и конец этой ветки????????????
        # Но это если self.SetSm[i0] не пересекается с StHead
        if (SmHead + self.Sm[i0] == self.target and
                not (self.SetSm[i0] & StHead) ):
            self.Res.append(Head + self.LstSm[i0])
            self.Stack -= 1
            return "s"

        # Сумма головы списка, включая и i0-й элемент
        NewSmHead = SmHead + self.Cands2[i0]
        # Если это слишком много - закончим
        # Если дальше добавлять в список, то будет ещё больше
        # Поэтому конец этой ветви.
        if NewSmHead > self.target:
            self.Stack -= 1
            return "n"
        # Новая голова списка - добавили //i0-й элемен
        NewHead = Head + self.LstVal[i0]
        # Если как раз цель - включили в результат
        # И продолжать с этим i0 - нет смысла: если что-то прибавлять,
        # то будет уже больше цели.
        if NewSmHead == self.target:
            # self.Res.add(tuple(NewHead))
            self.Res.append(NewHead)
            self.Stack -= 1
            #return "e"
            return "n"
        StHead1 = StHead | {self.SetCnd[i0]}
        # Значит ещё меньше цели
        # Пытаемся продолжить список дальше
        #for i in range(i0+1, self.Len):
        i = i0 + 1
        while i < self.Len:
            Code = self.FindSumFromSt(i, NewHead, NewSmHead, StHead1)
            if Code == "n":
                i += 1
                continue
            elif Code == "s":
                break

        self.Stack -= 1
        return "n"


cand = [2, 3, 5]
target = 8
cand = [2,3,6,7]
target = 7
#cand = [2]
#target = 1
a = Solution()
Res = a.combinationSum(cand, target)
print(Res)


