import timeit

# РђР»РіРѕСЂРёС‚Рј Р•РІРєР»РёРґР°
a = 50
b = 130
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
# print(a + b)

from random import randint


# РђР»РіРѕСЂРёС‚Рј СЃРѕСЂС‚РёСЂРѕРІРєРё РїСѓР·С‹СЂСЊРєРѕРј
def bubble(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
    return(array)


N = 5
a = []
for i in range(N):
    a.append(randint(1, 100))
print(bubble(a))


# РђР»РіРѕСЂРёС‚Рј Р±РёРЅР°СЂРЅРѕРіРѕ РїРѕРёСЃРєР°
def binary_search(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    if len(lys) == 1:
        return lys[0]
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


# print(binary_search([10,20,30,40,50], 20))
print(timeit.timeit("binary_search([1,4,5,6,7,10,20,30,40,50], 20)",
                    setup="from __main__ import binary_search", number=1))


# РђР»РіРѕСЂРёС‚Рј Р±РёРЅР°СЂРЅРѕРіРѕ РїРѕРёСЃРєР° (СЂРµРєСѓСЂСЃРёРІРЅС‹Р№)
def recursive_binary_search(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = recursive_binary_search((arr[mid:]), target)
            return mid + callback_response
        else:
            return recursive_binary_search((arr[:mid]), target)
        

# print(recursive_binary_search([10,20,30,40,50,60], 20))
print(timeit.timeit("recursive_binary_search([1,4,5,6,7,10,20,30,40,50], 20)",
                    setup="from __main__ import recursive_binary_search", number=1))
