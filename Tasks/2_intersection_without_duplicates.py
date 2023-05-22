'''
    Вам дано 2 набора чисел arr1 и arr2 в виде списка Python. Необходимо вернуть список, состоящий из элементов пересечения. Дубликаты необходимо удалить.

    Напишите функцию pure_intersection, которая будет возвращать список с уникальными элементами пересечения.

    Функция pure_intersection принимает на вход:

    arr1 - первый список с числами
    arr2 - второй список с числами
    Важно: Если пересечение пустое, то возвращаем пустой список.
'''

# my
def pure_intersection(arr1, arr2):
    res = []
    for num in set(arr1):
        if num in arr2:
            res.append(num)
    return res


result = pure_intersection([1, 3, 3], [6, 3, 3])
print(result)


# platform 1
def pure_intersection2(arr1, arr2):
    res = []
    for el in arr1:
        if el in arr2:
            res.append(el)
    res = list(set(res))
    return res


# platform 2
def pure_intersection3(arr1, arr2):
    return list(set(arr1).intersection(set(arr2)))
