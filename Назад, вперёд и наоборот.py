'''
На вход программе подается строка текста из натуральных чисел.
Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами
соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
Если в списке нечетное количество элементов, то последний остается на своем месте.
'''

numbers = input().split()
length = len(numbers)

for i in range(0, length - length % 2, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(*numbers)