# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#   Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random


def product(lst: list) -> list:
    product_elements = []
    while len(lst) > 1:
        product_elements.append(lst[0] * lst[-1])
        del lst[0]
        del lst[-1]
    if len(lst) == 1:
        product_elements.append(lst[0] ** 2)
    return product_elements


size = int(input('Enter the number of items: '))
lst = [random.randint(0, 10) for i in range(size)]

print(lst, end='')
print(' =>', product(lst))
