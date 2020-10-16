"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
user_number = int(input('Введите целое число\n>>>'))
max_number = 0
while user_number != 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10
print(max_number)
