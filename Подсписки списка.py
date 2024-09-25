'''
Подсписок — часть другого списка. Подсписок может содержать один элемент,
несколько или даже ни одного. Например, [1], [2], [3] и [4] —
подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4],
но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 2 и 4 во
втором списке не смежные (они разрываются элементом 3). Пустой список — 
подсписок любого списка. Сам список — подсписок самого себя, то есть 
список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы.
Из данной строки формируется список. Напишите программу,
которая выводит список, содержащий все возможные подсписки списка,
включая пустой список.
'''

def combination(string):
    my_list = [[]]
    string = string.split()

    for i in range(1, len(string) + 1):
        for j in range(len(string) - i + 1):
            my_list.append(string[j:j+i])

    return my_list

print(combination(input()))