#Разработать программу, которая во введенном тексте все строчные согласные буквы русского алфавита заменяет на знак "%",
#подсчитывает количество гласных и все цифры заменяет на знак "*".
#На печать выдать исходный текст, количество гласных и преобразованный текст.

glasnie = set('аяеэоёиыуюАЯЕЭЩЁИЫУЮ')
soglasnie = set('бвгдйжзклмнпрстфхцчшщ')
cifri = set('1234567890')


text = ''' Задание. 4.Разработать программу, которая во введенном тексте все строчные согласные буквы русского алфавита заменяет на знак "%", подсчитывает количество гласных и все цифры заменяет на знак "*".
На печать выдать исходный текст, количество гласных и преобразованный текст.'''

# Заменяем строчные согласные на '%'
s = "".join(map(lambda x: '%' if x in soglasnie else x, text))
# Заменяем цифры на '*'
s = "".join(map(lambda x: '*' if x in cifri else x, s))
# Подсчитываем количество гласных
numder_of_glassnie = sum(text.count(c) for c in glasnie)

print('Исходный текст:')
print(text)
print()
print('Количество гласных: {}'.format(numder_of_glassnie))
print()
print('Преобразованный текст:')
print(s)
