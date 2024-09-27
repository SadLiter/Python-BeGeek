'''
Дано натуральное число. Напишите программу, которая вычисляет:
количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи
(если цифр больших семи нет, то вывести 1,
если такая цифра одна, то вывести ее);
сколько раз в нем встречаются цифры 0 и 5 (всего суммарно).
'''

def task(number):
    counter3 = 0
    last_counter = 0
    even_counter = 0
    total_more_5 = 0
    multi_more_7 = 1
    counter_0_5 = 0

    for digit in str(number):
        digit = int(digit)
        if digit == 3:
            counter3 += 1
        if digit == number % 10:
            last_counter += 1
        if digit % 2 == 0:
            even_counter += 1
        if digit > 5:
            total_more_5 += digit
        if digit > 7:
            multi_more_7 *= digit
        if digit == 0 or digit == 5:
            counter_0_5 += 1

    return (counter3, last_counter, even_counter,
            total_more_5, multi_more_7, counter_0_5) 

print(*task(int(input())), sep="\n")