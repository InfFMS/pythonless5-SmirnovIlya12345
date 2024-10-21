# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from math import log10
from random import randint
a=[]
b=int(input())
for i in range(b):
    a.append(randint(10,100000))
print(a)
a1=[]
for i in range(b):
    if (round(log10(a[i])+0.5)==2 and a[i]%11==0) or (round(log10(a[i])+0.5)==3 and a[i]%111==0) or (round(log10(a[i])+0.5)==4 and a[i]%1111==0) or (round(log10(a[i])+0.5)==5 and a[i]%11111==0):
        a1.append(a[i])
print(a1)