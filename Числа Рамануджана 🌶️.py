'''
Сриниваса Рамануджан – индийский математик, славившийся своей
интуицией в области чисел. Когда английский математик Годфри
Харди навестил его однажды в больнице, он обмолвился, что
номером такси, на котором он приехал, было 1729, такое
скучное и заурядное число. На что Рамануджан ответил:
"Нет, нет! Это очень интересное число. Это наименьшее
число, выражаемое как сумма двух кубов двумя разными

способами". Напишите программу, которая находит
аналогичные интересные числа. В ответе запишите первые 5
чисел в порядке возрастания, включая число 1729
'''

def find_interesting_number():
    for a in range(1, 50):
        for b in range(1, 50):
            for c in range(1, 50):
                for d in range(1, 50):
                    if (((a**3 + b**3) == (c**3 + d**3)) and
                        (a != b and a != c and a != d and b != c and b != d and c != d)):
                        yield (a**3 + b**3)

interesting_numbers = sorted(set(find_interesting_number()))
print(*interesting_numbers)