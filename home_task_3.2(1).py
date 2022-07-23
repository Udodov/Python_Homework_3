# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#   Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
import math


def product(lst: list) -> list:
    return [lst[i] * lst[-i - 1] for i in range(math.ceil(len(lst) / 2))]
    # rounding to the nearest value greater than half the length of the fibonacci_list


size = int(input('Enter the number of items: '))
lst = [random.randint(0, 10) for i in range(size)]

print(lst, end='')
print(' =>', product(lst))
