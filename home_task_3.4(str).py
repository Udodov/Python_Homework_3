# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#   Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def convert(num: int) -> str:
    binary_number = ''
    while num > 0:
        binary_number = str(num % 2) + binary_number
        num = num // 2
    return binary_number


num = int(input('Enter an integer decimal number: '))
print(f'The decimal number {num} in binary notation looks like this -> ', convert(num))
