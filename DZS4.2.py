def rock_paper_scissors():
# Запрос выбора пользователя
    player = int(input("1 - камень, 2 - ножницы, 3 - бумага. Введите ваш выбор: "))
# Варианты выбора компьютера для примера
    computer = 1 # В этом примере компьютер всегда выбирает камень
# Определение и вывод результата игры
    if player == computer:
        print("Ничья!")
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("Вы выиграли!")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("Вы проиграли!")
    else:
        print("Неверная команда. Попробуйте снова.")

def guess_the_number():
    number = 7 # Загаданное число для примера
    while True:
# Запрос числа от пользователя
        guess_num = int(input('Введите число: '))
# Проверка и вывод подсказки
    if guess_num > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif guess_num < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Поздравляю, вы угадали! Возврат в главное меню.')
    break # Выход из цикла, если число угадано

def main_menu():
    while True:
# Вывод меню выбора игры
        print('Во что хотите поиграть?')
        game = int(input('1 - Камень, ножницы, бумага; 2 - Угадай число; 3 - Выйти: '))
# Вызов соответствующей функции в зависимости от выбора
    if game == 1:
        rock_paper_scissors()
    elif game == 2:
        guess_the_number()
    elif game == 3:
        print('Выход из программы.')
        break # Выход из цикла и завершение программы
    else:
        print('Неверная команда. Попробуйте снова.')
# Запуск главного меню
main_menu()