from tkinter import *  # Tk_interface - GUI для Python
from random import randrange, randint


def Addition(limit=10):  # сложение
    lst = [0, ' + ', 0, ' = ', 0]
    result = randrange(3, limit + 1)
    a = randrange(1, result)
    b = result - a
    lst[0], lst[2], lst[4] = a, b, result
    return lst


def Subtraction(limit=10):  # вычитание
    lst = [0, ' - ', 0, ' = ', 0]
    a = randrange(3, limit + 1)
    result = randint(1, a)
    b = a - result
    lst[0], lst[2], lst[4] = a, b, result
    return lst


def GenSum(limit=10):  # генерация примера
    x = randint(0, 1)
    if x == 1:
        return Addition(limit)
    else:
        return Subtraction(limit)


def GenSum2(limit=10, act=2):  # генерация примера
    if act == 1:
        return GenSum(limit)
    else:
        sum1 = GenSum(limit)
        pass


for _ in range(10):
    rez = GenSum2(20, 1)
    print(*rez)
