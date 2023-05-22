# Вам дан набор чисел в виде списка Python. Необходимо найти медиану этого числового ряда.
# Медиана — число, которое находится в середине упорядоченного по возрастанию ряда.

# Напишите функцию find_median, которая будет возвращать одно число - медианное значение.
# Если переданный в функцию список окажется пустым - верните None.
#
# Функция find_median принимает на вход arr - исходный список с числами.
#
# Пример 1:
#
# find_median([1, 5, 2, 3, 6])
# Ответ: 3
#
# Пример 2:
#
# find_median([100, 5, 2, 4, 3, 6])
# Ответ: 4.5
#
# Примечание: Если в выборке четное число элементов, то за медиану нужно
# взять среднее между центральными элементами (после упорядочивания).

# my
def find_median(arr):
    if not arr:
        return None
    arr = sorted(arr)

    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[(len(arr)//2) - 1])/2

    return arr[len(arr)//2]


num = find_median([1, 5, 2, 3, 6])
print(num)


# from platform
def find_median(arr):
    if not arr:
        return None
    n = len(arr)
    ind = n // 2
    if n % 2:
        return sorted(arr)[ind]
    return sum(sorted(arr)[ind-1:ind+1]) / 2