# Итератор - класс, у которого есть __next__
# Итерируемый объект - есть метод __iter__

class multifilter:
    def judge_half(self, pos, neg):
        return pos >= neg

    def judge_any(self, pos, neg):
        return pos > 0

    def judge_all(self, pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterator = iter(iterable)
        self.funcs = funcs
        self.judge = judge

    def __next__(self):
        while True:
            elem = next(self.iterator)
            pos, neg = 0, 0
            for func in self.funcs:
                if func(elem):
                    pos += 1
                else:
                    neg += 1
            if self.judge(self, pos, neg):
                return elem

    def __iter__(self):
        return self


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]