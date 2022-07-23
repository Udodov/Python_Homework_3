# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#   Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def fractional_list(lst: list) -> list:
    fractional_part = [round((lst[i] % 1), 2) for i in range(len(lst))]
    return round((max(fractional_part) - min(fractional_part)), 2)


size = int(input('Enter the number of items: '))
lst = [round(uniform(0, 100), 2) for i in range(size)]

print(lst, end='')
print(' =>', fractional_list(lst))
