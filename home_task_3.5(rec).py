# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#   Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# F(-n)=(-1)**(n+1)*F(n)


def right_part(n: int) -> int:
    if n in [1, 2]:
        return 1
    else:
        return right_part(n - 1) + right_part(n - 2)


def left_part(n: int) -> int:
    if n in [-1, 0]:
        return 1
    else:
        return left_part(n - 2) - left_part(n - 1)


fibonacci_list = []
k = int(input('Enter a number for the Fibonacci fibonacci_list: '))

for positive in range(1, k + 1):
    fibonacci_list.append(right_part(positive))
for negative in range(1, k + 2):
    fibonacci_list.insert(0, left_part(negative))

print(fibonacci_list)
