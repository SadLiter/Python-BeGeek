'''
На вход программе подается натуральное число n.
Напишите программу, которая выводит первые n строк треугольника Паскаля.
'''

def PrintPasTriangle(rows):
    row = [1]
    for _ in range(rows):
        print(*row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


PrintPasTriangle(int(input()))
