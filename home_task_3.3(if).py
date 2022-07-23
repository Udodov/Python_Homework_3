# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#   Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def fractional_list(lst: list) -> list:
    fractional_part = []
    for i in range(len(lst)):
        fractional_part.append(round((lst[i] % 1), 2))
    return fractional_part


size = int(input('Enter the number of items: '))
lst = [round(uniform(0, 100), 2) for i in range(size)]

fractional = fractional_list(lst)
maximum, minimum = fractional[0], fractional[0]

for i in range(1, len(fractional)):
    if fractional[i] >= maximum:
        maximum = fractional[i]
    if fractional[i] < minimum:
        minimum = fractional[i]
difference = maximum - minimum

print(f'{lst} => {difference}')
print(f'{fractional}--> maximum={maximum}, minimum={minimum}')
