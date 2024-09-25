'''
На вход программе подается число n.
Напишите программу, которая создает
и выводит построчно вложенный список, состоящий из
n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
'''

def create_list(n):
    my_list = []

    for i in range(1, n+1):
        my_list.append(list(range(1, i+1)))

    return my_list

n = int(input())

print(*create_list(n), sep='\n')