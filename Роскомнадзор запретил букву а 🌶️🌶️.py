'''
Необходимо написать программу, реализующую алгоритм написания этой песни.
Алгоритм выводит в конце предложения следующую в алфавитном порядке букву,
если она встречается в строке текста, а очередную строку отображает уже без этой буквы.
'''

def roskomnadzor(word):
    word = word + ' запретил букву '
    letters = [chr(i) for i in range(1072, 1104)]
    
    for letter in letters:
        if letter in word:
            string = (word + letter).split()
            string = " ".join(string)
            print(string)
            word = word.replace(letter, '')

roskomnadzor(input())