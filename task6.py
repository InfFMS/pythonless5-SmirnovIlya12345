# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint
a1=[]
a2=[]
b=int(input())
for i in range(b):
    a1.append(randint(0, 10))
for i in range(b):
    a2.append(randint(0, 10))
a=a1+a2
print(a)
a3=[0]*b
a4=[0]*b
for i in range(b):
    a3[i]=a1[-i-1]
for i in range(b):
    a4[i]=a2[-i-1]
r=a3+a4
print(r)
