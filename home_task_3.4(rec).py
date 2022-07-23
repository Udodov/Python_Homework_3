# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#   Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def convert(num: int) -> int:
    if num == 0:
        return
    convert(num // 2)
    print(num % 2, end='')


num = int(input('Enter an integer decimal number: '))
print(f'The decimal number {num} in binary notation looks like this -> ', end='')
convert(num)
