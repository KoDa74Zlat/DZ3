def digits_summ(num):
    summ = 0
    while num > 0:
        digit = num % 10 # Получаем последнюю цифру
        summ += digit # Добавляем цифру к сумме
        num //= 10 # Удаляем последнюю цифру из числа
    print('Сумма цифр:', summ)

def max_digit(num):
    maximum = 0
    while num > 0:
        digit = num % 10 # Получаем последнюю цифру
        if digit > maximum: # Сравниваем с текущим максимумом
            maximum = digit # Обновляем максимум
        num //= 10 # Удаляем последнюю цифру из числа
    print('Максимальная цифра:', maximum)

def min_digit(num):
    minimum = num % 10 # Начинаем с последней цифры
    while num > 0:
        digit = num % 10 # Получаем последнюю цифру
        if digit < minimum: # Сравниваем с текущим минимумом
            minimum = digit # Обновляем минимум
        num //= 10 # Удаляем последнюю цифру из числа
    print('Минимальная цифра:', minimum)
while True:
    num = int(input('Введите число: ')) # Запрос числа упользователя
    action = int(input('Введите номер действия: 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра: ')) # Запрос действия
    if action == 1:
        digits_summ(num) # Вызов функции для суммы цифр
    elif action == 2:
        max_digit(num) # Вызов функции для максимальной цифры
    elif action == 3:
        min_digit(num) # Вызов функции для минимальной цифры
    else:
        print('Ошибка: неверная команда.') # Обработка неверного ввода