# 4. Напишите программу, которая будет преобразовывать десятичное числов двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
def conv_bin(num: int):
    my_list = []

    while num > 0:
        my_list.insert(0, num % 2)
        num //= 2

        print(*my_list, sep="")


conv_bin(int(input('Введите число ')))