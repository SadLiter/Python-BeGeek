'''
На вход программе подаются две строки: на одной – символы,
на другой – число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход
список и число, задающее размер чанка (куска), а возвращает
список из чанков (кусков) указанной длины.
'''

def chunked(string, n):
    result_list = []
    string = string.split()

    for i in range(0, len(string), n):
        result_list.append(string[i:i+n])

    return result_list

print(chunked('a b c d e b', 3))

'''
string, n = input().split(), int(input())
print([string[i:i+n] for i in range(0, len(string), n)])
'''