"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""


int_number = 15
street = 'Ноябрьская'
float_number = 177.37

new_number = float_number/int_number
new_number2 = float_number//int_number

user_number = int(input('Введите целое число\n>>>'))
user_name = input('Введите своё имя\n>>>')

print(f'{user_number} * {int_number} = {user_number*int_number}')
print(f'{new_number} = {float_number} / {int_number}')
print(f'{float_number/int_number} = {float_number} / {int_number}')
