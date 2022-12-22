# Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)


from random import random
 
def float(a):
    return sum(a) / len(a)
 
n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество стобцов матрицы: "))
A = []
 
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(int(random() * 10))
    A.append(arr)
 
for arr in A:
    print(arr, float(arr))
