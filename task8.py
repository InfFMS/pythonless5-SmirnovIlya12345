# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from random import randint
a=[]
b=int(input())
for i in range(b):
    a.append(randint(10,100000))
print(a)
a1=[]
def are_there_any_pretty_numbers(a):
    for i in range(b):
        c=[a[i] for a[i] in a if(a[i]<100 and a[i]%11==0) or (a[i]>99 and a[i]<1000 and a[i]%111==0) or (a[i]>999 and a[i]<10000 and a[i]%1111==0) or (a[i]>9999 and a[i]%11111==0)]
    print(c)
are_there_any_pretty_numbers(a)
