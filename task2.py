# 2 Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.

N = int(input('введите N: '))

my_list = []
for i in range(2, N):
    if N % i == 0:
        j = i
        count = 0
        for idx in range(2, j + 1):
            if j % idx == 0:
                count += 1
        if count == 1:
            my_list.append(i)

print(f'Список простых множителей: {my_list}')

        
