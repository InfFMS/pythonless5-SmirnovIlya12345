# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами
from random import randint
a=[]
b=int(input())
for i in range(b):
    a.append(randint(0, 1000))
print(a)
print(b)
print(a[b-1])
c=[0]*b
for i in range(b):
    c[i]=a[-i-1]
print(c)
d=0
for i in range(b):
    if a[i]%111==0 and a[i]>0:
        d+=1
if d==0:
    print("NO")
else:
    print("YES")
e=[0]*(b-2)
for i in range(b-2):
    e[i]=a[i+1]
print(e)