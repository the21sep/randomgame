# Игрок вводит свою догадку в переменную user_number,
# if user_number и number совпадают, то выводится фраза «Это верно, я загадал число n», где n — загаданное число.
# # if не совпадают, то выводится «Не угадал».
# number = 3
#
# print("Попробуй угадать число от 0 до 5!")
#
# user_number = int(input("Введи число: "))
# if user_number == number:
#     print(f'Это верно, я загадал число {number} ')
# else:
#     print('Не угадал ')

# import random
#
# number = random.randint(0, 5)
#
# print("Попробуй угадать число от 0 до 5!")
#
# user_number = int(input("Введи число: "))
#
# attempts = 3
# while user_number != number or attempts == 0:
#     print('Не угадал ')
#     user_number = int(input("Введи число: "))
#     attempts -= 1
# if user_number == number:
#     print(f'Это верно, я загадал число {number} ')
#     print('Ты выиграл!')
# else:
#     print('Ты проиграл!')

import random

number = random.randint(0, 5)

print("Попробуй угадать число от 0 до 5!")

user_number = int(input("Введи число: "))

attempts = 1

while user_number != number and attempts < 3:
    print("Не угадал")
    user_number = int(input("Введи число: "))
    attempts += 1

if user_number == number:
    print("Это верно, я загадал число", number)
    print("Ты выиграл")
else:
    print("Ты проиграл")