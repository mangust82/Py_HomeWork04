# Вычислить число c заданной точностью d 
# Пример: 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = int(input('введите заданную точность d число знаков после запятой: '))

Pi = 3
for i in range(2, 10000, 4):
    Pi = Pi + 4 / (i * (i+1) * (i+2)) - 4 / ((i+2) * (i+3) * (i+4))
print(round(Pi, d))

