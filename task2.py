# Задание 2
# Дана переменная, в которой хранится число (год).
# Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.
#
# Пример работы программы: 1.
#
# year = 2020
# Результат:
# Високосный год
#
# year = 2019
# Результат:
# Обычный год

# Любой год, который делится на 4 без остатка, является високосным годом!!

year = int(input('Введите год: '))

if year%4 == 0:
    print('Високосный год')
else:
    print('Обычный год')
