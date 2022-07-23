# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#   Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# F(-n)=(-1)**(n+1)*F(n)


def number_fibonacci(k: int) -> list:
    fibonacci_list = []
    fib_1, fib_2 = 1, 1

    for i in range(k):
        fibonacci_list.append(fib_1)
        fib_1, fib_2 = fib_2, fib_1 + fib_2  # fib_1 = fib_2, fib_2 = fib_1 + fib_2

    fib_1, fib_2 = 0, 1

    for i in range(k + 1):
        fibonacci_list.insert(0, fib_1)      # fib_1 is added to the fibonacci_list by index [0].
                                                # All elements after the element are shifted to the right
        fib_1, fib_2 = fib_2, fib_1 - fib_2  # fib_1 = fib_2, fib_2 = fib_1 - fib_2

    return fibonacci_list


k = int(input('Enter a number for the Fibonacci fibonacci_list: '))

print(number_fibonacci(k))
