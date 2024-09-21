'''
Дана строка текста, состоящая из букв русского алфавита 
"О" и "Р". Буква "О" соответствует выпадению Орла,а буква "Р" - выпадению Решки
Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
'''

def counter(string):
    count = 0
    max_count = 0

    for i in range(len(string)):
        if string[i] == 'Р':
            count += 1
        else:
            if count >= max_count:
                max_count = count
            count = 0

    if count > max_count:
        max_count = count

    return max_count

string = input()

print(counter(string))