import random

# Задание 1. В одномерном массиве, заполненном случайными числами, 
# найти сумму элементов, стоящих на четных позициях (индексах).
print(" Задание 1")
n1 = int(input("Введите размер массива: "))
arr1 = [random.randint(1, 100) for _ in range(n1)] # заполнен случайными числами
print("Массив:", arr1)

sum_even = sum(arr1[i] for i in range(0, n1, 2))
print("Сумма элементов на четных индексах:", sum_even)



# Задание 2. В одномерном массиве найти все элементы, значение которых 
# больше среднего арифметического всего массива. Вывести их значения и индексы.

print("Задание 2 ")
n2 = int(input("Введите размер массива: "))
arr2 = []
print("Введите элементы массива:")
for _ in range(n2):
    arr2.append(int(input()))

avg = sum(arr2) / len(arr2)
print("Среднее арифметическое:", avg)
print("Элементы больше среднего:")
for i, val in enumerate(arr2):
    if val > avg:
        print(f"Значение: {val}, Индекс: {i}")



# Задание 3. Дан массив целых чисел. Создать новый массив, 
# который содержит только уникальные (неповторяющиеся) элементы исходного массива.

print(" Задание 3")
n3 = int(input("Введите размер массива: "))
arr3 = []
print("Введите элементы массива:")
for _ in range(n3):
    arr3.append(int(input()))

new_arr = list(dict.fromkeys(arr3))
print("Новый массив с уникальными элементами:", new_arr)



# Задание 4. Для матрицы (двумерного массива) найти сумму всех элементов.

print(" Задание 4")
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix4 = []
print("Введите элементы матрицы:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix4.append(row)

total = sum(sum(row) for row in matrix4)
print("Сумма всех элементов матрицы:", total)



# Задание 5. Для квадратной матрицы найти сумму элементов на главной диагонали.

print(" Задание 5")
n5 = int(input("Введите размер квадратной матрицы: "))
matrix5 = []
print("Введите элементы матрицы:")
for i in range(n5):
    row = []
    for j in range(n5):
        row.append(int(input()))
    matrix5.append(row)

diag_sum = sum(matrix5[i][i] for i in range(n5))
print("Сумма элементов на главной диагонали:", diag_sum)



# Задание 6. Для одномерного массива выполнить циклический сдвиг вправо на k элементов.

print(" Задание 6")
n6 = int(input("Введите размер массива: "))
arr6 = []
print("Введите элементы массива:")
for _ in range(n6):
    arr6.append(int(input()))

k = int(input("Введите k: "))
k = k % n6
result = arr6[-k:] + arr6[:-k] if k else arr6[:]
print("Массив после сдвига вправо на", k, "элементов:", result)
