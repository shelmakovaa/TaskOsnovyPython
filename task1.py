# Задание 1
# Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
# Напишите код, который проверяет какая из этих строк длиннее.
#
# Примеры работы программы:
# 1.
#
# phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
# phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
#
# Результат:
# Фраза 1 длиннее фразы 2 2.
#
# phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
# phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
# Результат:
# Фраза 2 длиннее фразы 1 3.
#
# phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
# phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
# Результат:
# Фразы равной длины

phrase_1 = input('Введите фразу 1: ')
phrase_2 = input('Введите фразу 2: ')

if len(phrase_1) > len(phrase_1):
    print("Фраза 1 длиннее фразы 2")
else:
    print("Фраза 2 длиннее фразы 1")