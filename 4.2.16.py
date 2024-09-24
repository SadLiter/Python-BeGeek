# Дополните приведенный код так, чтобы он выводил единственное число:
# сумму всех чисел списка list1, разделённую на общее количество всех чисел.

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = sum(sum(numbers) for numbers in list1)
counter = sum(len(numbers) for numbers in list1)

print(total / counter)