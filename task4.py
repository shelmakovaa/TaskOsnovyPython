# Задание 4
# Вам нужно написать программу для подбора упаковок по размерам товара.
# Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):
#
# Используйте следующие правила:
#
# если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
# если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
# если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
# во всех остальных случаях выводите "Коробка №3".
# Пример работы программы:
# 1.
#
# width = 15
# length = 55
# height = 15
# Результат:
# Коробка №3
#
# width = 45
# length = 205
# height = 45
# Результат:
# Упаковка для лыж

width = int(input("Введите ширину: "))
length = int(input("Введите длину: "))
height = int(input("Введите высоту: "))

if width <= 15 and length <= 15 and height <= 15:
    print('Коробка №1')
elif width > 200 or length > 200 or height > 200:
    print('Упаковка для лыж')
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
    print('Коробка №2')
else:
    print('Коробка №3')