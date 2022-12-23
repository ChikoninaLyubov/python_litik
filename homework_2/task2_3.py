# 3. Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int
num = int(input('Введите цифру : '))
num_list = list(range(num))
my_list = []
print(num_list)
from random import randrange

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    num_list[n_1], num_list[n_2] = num_list[n_2], num_list[n_1]

print(num_list)



