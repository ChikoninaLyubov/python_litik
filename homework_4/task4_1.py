#1. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# from random import randrange, choice

import random

# создаем словарь: ключ значение ( от 0 до 100)
def create_dictionary():
    degree = int(input('Enter the k - degree:'))
    my_dict ={}
    for n in range(degree, -1, -1):
        my_dict[n] = random.randint(0,101)
    return my_dict

def polynomial(my_dict:dict) -> str:
    new_equation = []
    for key, value in my_dict.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0'
    # new_equation = new_equation.replace('+-', '-'), тк от 0 до 100 будет только плюс
    new_equation = new_equation.replace(' 1*x', ' x')
    new_equation = new_equation.replace('*x**0', '')
    new_equation = new_equation.replace('x**1', 'x')
    return new_equation

# new_equation=polynomial(my_dict)
# print(new_equation)

def main():
   
    my_dict = create_dictionary()
    print(my_dict)

    new_equation1=polynomial(my_dict)
    print(new_equation1)
 

if __name__ == "__main__":
    main()    