"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""
inter = float(input('Результат первого дня\n>>>'))
result = float(input('Желаемый результат\n>>>'))
day = 1

while inter < result:
    inter = inter * 1.1
    day += 1
print(f'на {day}-й день спортсмен достиг результата — не менее {result} км.')