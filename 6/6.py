str = '''1. Задание Дан текст. Все слова, длина которых в 2 раза меньше длины слова максимальной длины, заменить на слово максимальной длины.
'''
print(str)

listWords = str.split()

idLongestWord = 0

for i in range(1, len(listWords)):
    if len(listWords[idLongestWord]) < len(listWords[i]):
        idLongestWord = i
word = listWords[idLongestWord].replace('.', '').replace(',', '')
dlz = int(len(word) / 2)

print('Самое длинное слово: {}'.format(word))
print()

s = " ".join(map(lambda x: word if len(x) == dlz else x, listWords))

print(s)
