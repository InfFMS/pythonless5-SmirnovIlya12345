# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
a=[]
b=int(input())
for i in range(b):
    a.append(int(input()))
a1=[]
a1.append(a[0])
for i in range(1, b):
    for j in range(len(a1)):
        c=0
        if a[i]==a1[j]:
            c=1
            break
    if c==0:
        a1.append(a[i])
print(a1)

