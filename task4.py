# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
from os import system

system("cls")

k = int(input('Enter degree of number: '))

polynominal = ''
for i in range(k, 0, -1):
    polynominal += str(random.randrange(0,101))+'*x^' + str(i) + ' + '
polynominal += str(random.randrange(0,101)) + ' = 0'
print(polynominal)

with open('polynominal.txt', "w") as f_obj:
    print(polynominal, file=f_obj, end='')