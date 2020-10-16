"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
"""

random_number = input('Введите целое число\n>>>')
second_number = int(random_number+random_number)
third_number = int(random_number+random_number+random_number)
print(int(random_number) + second_number + third_number)
