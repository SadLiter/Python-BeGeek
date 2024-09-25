'''
На вход программе подается число n
Напишите программу, которая создает и выводит построчно список, состоящий из
n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
'''

def create_matrix(n):
    my_list = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            my_list[i][j] = j+1

    return my_list

n = int(input())

print(*create_matrix(n), sep='\n')

