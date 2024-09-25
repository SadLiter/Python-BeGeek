'''
На вход программе подается строка текста, содержащая символы.
Напишите программу, которая упаковывает последовательности
одинаковых символов заданной строки в подсписки.
'''

def duplicates(string):
    string = string.split()
    char_list = [[string[0]]]

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            char_list[-1].append(string[i])
        else:
            char_list.append([string[i]])

    return char_list

print(duplicates(input()))