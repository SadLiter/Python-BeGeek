'''
Напишите программу для определения,
является ли число произведением двух чисел из данного набора.
Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
'''

size = int(input())
number_list = [int(input()) for _ in len(size)]

last_number = int(input())

def answer(number_list, last_number):
    for i in range(len(number_list)-1):
        for j in range(i+1, len(number_list)):
            if number_list[i] * number_list[j] == last_number:
                return "ДА"
            
    return "НЕТ"

print(answer(number_list, last_number))
