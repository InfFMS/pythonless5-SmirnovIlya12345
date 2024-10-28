# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
from random import randint
from math import acos
from math import sqrt
a=[]
b=[]
d=int(input())
for i in range(d):
    a.append(randint(-10,10))
    b.append(randint(-10,10))
print(a)
print(b)
c=0
lea=0
leb=0
for i in range(d):
    lea+=a[i]*a[i]
    leb+=b[i]*b[i]
for i in range(d):
    c+=a[i]*b[i]
print(acos(c/sqrt(lea)/sqrt(leb))*180/3.141592653589793238462643)