from os import system

system("cls")

#считываем строку с многочленами из 2-х файлов
with open('polynominal.txt', "r") as f1_obj:
   pol1 = f1_obj.readline()
with open('secondfile.txt', "r") as f2_obj:
   pol2 = f2_obj.readline()

# Делим строку по разделителю ' ' в список и подстроку по разделителю '*x^' 
# и формируем словарь {"степень": "множитель"}
my_list1 = pol1.split(' ')
my_list2 = pol2.split(' ')

dict1 = {}
flag = 1
for el in my_list1:
    if el.find('*x^') != -1:
       dict1[el.split('*x^')[1]] = int(el.split('*x^')[0]) * flag
    elif el == '+':
        flag = 1
    elif el == '-':
        flag = -1

dict2 = {}
flag = 1
for el in my_list2:
    if el.find('*x^') != -1:
       dict2[el.split('*x^')[1]] = int(el.split('*x^')[0]) * flag
    elif el == '+':
        flag = 1
    elif el == '-':
        flag = -1

# Преобразуем во множество ключи и объединяем множества с результирующими степенями
mnog1 = set()
for el in dict1:
    mnog1.add(el)
mnog2 = set()
for el in dict2:
    mnog2.add(el)

mnog = mnog2.union(mnog1)

# Складываем множетели из двух словарей и формируем результирующий словарь
dictn = {}
for el in mnog:
    if dict1.get(el) is None:
        sum1 = 0
    else:
        sum1= int(dict1.get(el))
    if dict2.get(el) is None:
        sum2 = 0
    else:
        sum2= int(dict2.get(el))
    sum =sum1 + sum2
    dictn[el] = str(sum)

# Сортируем словарь
dictf = dict(sorted(dictn.items(), reverse=True))

# Формируем итоговую строку многочлена
com_str =''
for el in dictf:
    com_str += dictf.get(el) + '*x^' + el + ' + '

a0 = int(my_list1[-3].split(' = ')[0]) + int(my_list2[-3].split(' = ')[0])
com_str += str(a0) + ' = 0'

# Записываем в итоговый файл
with open('result.txt', "w") as res_obj:
    print(com_str, file = res_obj, end = '')

print(com_str)