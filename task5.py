# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
a=[]
b=int(input())
max=-10*100
c=0
for i in range(b):
    d=float(input())
    a.append(d)
    if d>max:
        max=d
        c=1
    elif d==max:
        c+=1
print(c)

