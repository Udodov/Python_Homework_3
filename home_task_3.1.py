# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#   Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def product(lst: list) -> int:
    prod = 0
    for i in range(1, len(lst), 2):
        prod += lst[i]
    return prod


size = int(input('Enter the number of items: '))
lst = [random.randint(0, 10) for i in range(size)]

print(lst)
print('Sum of odd elements =', product(lst))
