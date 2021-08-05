from math import sqrt


# Среднее арифметическое значение
def middle_value(array):
    sum = 0
    length = len(array)
    if length > 0:
        for element in array:
            sum += element
    return sum / length


# Медиана
def mediana(array):
    length = len(array)
    if length % 2 != 0:
        return array[length // 2]
    else:
        a = array[length // 2 - 1]
        b = array[length // 2]
        return (a + b) / 2


# Квартили (делят выборку на 4 равные части)
def kvartiles(array):
    kv = [mediana(array)]
    arr_1 = []
    arr_2 = []
    for elem in array:
        if elem < mediana(array):
            arr_1.append(elem)
        elif elem > mediana(array):
            arr_2.append(elem)
    kv.append(mediana(arr_1))
    kv.append(mediana(arr_2))
    kv.sort()
    return kv


# Мода
def moda(array):
    max = 0
    length = len(array)
    if length > 0:
        for element in array:
            if element > max:
                max = element
    return max


# Дисперсия
def variance(array):
    mv = middle_value(array)
    sum = 0
    length = len(array)
    if length > 0:
        for element in array:
            x = element - mv
            sum += x * x
    return sum / (length - 1)


# Стандартное отклонение / Среднее квадратическое отклонение
def sd(array):
    return sqrt(variance(array))


# Стандартизация / Z-преобразование
# Среднее = 0, а Дисперсия = 1
def z_score(array):
    new_array = []
    mv = middle_value(array)
    std = sd(array)
    for element in array:
        new_array.append((element - mv) / std)
    return new_array
