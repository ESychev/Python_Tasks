rus_eng = {}
eng_rus = {}
text = '''Задание Написать программу на языке Python, создающую из русско-английского словаря англо-русский словарь (обязательно использовать словари(dict)).
Входные данные берутся из файла input.txt, выходные данные записываются в файл output.txt. Входные данные лексикографически отсортированы, и выходные данные тоже должны быть отсортированы! В выходной файл первым записать полученное количество английских слов!   Необходимо, чтобы во входном файле находилось, как минимум, 5 русских слов, которые имеют несколько английских значений.
На хорошую оценку по работе (8, 9 и 10) слова должны быть подобраны так, как в моём примере, чтобы в результате одно английское слово имело несколько русских значений.'''
print(text)
print('Начало работы')
with open('input01.txt', 'r') as inf, open('output01.txt', 'w') as outf:
    for line in inf:
        a = line.split('-')
        key = a[0].strip()
        value = a[1].strip()
        rus_eng[key] = value
        eng = value.split(',')
        for i in eng:
            i = i.strip()
            if i in eng_rus:
                eng_rus[i] = eng_rus[i] + ', ' + key
            else:
                eng_rus[i] = key
        print(' * ', end=' ')
    # Сортировка
    list_keys = list(eng_rus.keys())
    list_keys.sort()
    # Колво английских слов
    outf.write('{}\n'.format(len(eng_rus)))
    for i in list_keys:
        outf.write('{} - {}\n'.format(i, eng_rus[i]))

print('\nФайл output01.txt - записан')
