# 3 Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import random
from os import system

system('cls')

first_list = []
for i in range(30):
    first_list.append(random.randrange(0, 100))
print(f'Source list: {first_list}')

new_list = []
copy_list =first_list.copy()
print('Repeated elemens:')
for i in range(len(first_list)):
    flag = 0
    for j in range(i+1, len(first_list)):
        if first_list[i] == first_list[j]:
            flag = 1
            print(first_list[i], end=' ')
    if flag == 0:
        new_list.append(first_list[i])
print()

print(f'Result list: {new_list}')
