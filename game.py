import numpy as np
"""We'll try to wright a game 'Guess a number' """
# загадываем число, используя функцию-генератор случайного числа от 1 до 100
number = np.random.randint(1, 101) 
# создаем переменную-счетчик для подсчета попыток угадывания
count = 0

# пишем цикл, который будет позволять вводить и угадывать числа
while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100"))
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла