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
    result = ''
    counter = 3
    while counter:
        # counter = 1
        for i in range(len(s)):
            print(s[i], s[i] in result, s.count(s[i]))
            if s.count(s[i]) > 1:
                # counter += 1
                if s[i] not in result:
                    if s[i] != 'z':
                        result += alph[alph.index(s[i]) + 1]
                    else:
                        result += alph[0]

                elif s[i] in result:
                    result += s[i]
                s = s.replace(s[i], ' ', 1)
            else:
                if s[i] not in result:
                    print(f'{s[i]} not in result')
                    result += s[i]
            print(f'result {result}, s {s}')
        s = result
        result = ''
        print(f'stroke {s}, counter {counter}')
        print("#####")
        counter -= 1
    return result


print(replace_duplicates('zzzab'))
