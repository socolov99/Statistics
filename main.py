from statistics import *

arr = [157, 159, 161, 164, 165, 166, 167, 167, 167, 168, 169, 169, 170, 170, 170, 171, 171, 172, 172, 172, 172, 173,
       173, 175, 175, 177, 178, 178, 179, 185]

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 1, 8, 1, 8, 9, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1]

print('Среднее значение: ' + str(middle_value(arr)))
print('Медиана: ' + str(mediana(arr)))
print('Мода: ' + str(moda(arr)))
print('Дисперсия: ' + str(variance(arr)))
print('Стандартное отклонение: ' + str(sd(arr)))
print('Квартили: ' + str(kvartiles(arr)))
print('z-преобразование:' + str(z_score(arr)))
