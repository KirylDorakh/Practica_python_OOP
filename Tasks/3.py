'''
Напишите функцию replace_duplicates, которая принимает на вход произвольную строку s.
Функция должна заменять две одинаковые буквы на следующую по алфавиту букву.

Несколько важных моментов:

буквы не обязаны быть смежными (смежные - стоящие рядом; в строке 'abc' буквы a и b, а также b и c - являются смежными,
в то время как a и c - нет)
zz заменяем на a
строка s состоит из букв английского алфавита в строчном регистре
Повторяйте операцию, пока не останется никаких возможных замен. Функция должна вернуть строку с оставшимися буквами
в любом порядке.

Пример:

Дано: zzzab
Шаг 1: azab
Шаг 2: bzb
Шаг 3: cz
Результат: cz
'''

import string

alph = list(string.ascii_lowercase)


def replace_duplicates(s):
    counter1 = 1
    while counter1:
        counter1 = 0
        result = ''
        d1 = {}
        for i in range(len(s)):
            d1[s[i]] = s.count(s[i])
        for key, value in d1.items():
            if value == 1:
                result += key
            else:
                counter1 = value
                while value > 0:
                    if value // 2:
                        value -= 2
                        if key != 'z':
                            result += alph[alph.index(key) + 1]
                        else:
                            result += alph[0]
                    else:
                        value -= 1
                        result += key
        s = result

    return s


print(replace_duplicates('zzzab'))
