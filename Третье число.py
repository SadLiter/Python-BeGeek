'''
Дано натуральное число n(n>99).
Напишите программу, которая определяет
его третью (с начала) цифру.
'''

def third_number(number):
    while len(str(number)) >= 3:
        last_digit = number % 10
        number = number // 10

    if number % 1000 == 0:
        return 0
    else: return last_digit

number = int(input())
print(third_number(number))