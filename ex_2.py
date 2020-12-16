import math

print('4301 Санников')
print('y = sqrt(7.8 * sin(80deg12min)^3)/(5 ** 0.72)')

# y = sqrt(7.8 * sin(80deg12min)^3)/(5 ** 0.72)

coef = 7.8
pow_arg = 5

while True:
    try:
        degree = float(input('Градусы: '))
        break
    except:
        print ('Градусы должны быть числом.')
        continue   

while True:
    try:
        seconds = float(input('Секунды: '))
        break
    except:
        print ('Градусы должны быть числом.')
        continue   

while True:
    try:
        pow_ = float(input('Показатель степени: '))
        break
    except:
        print ('Показатель степени должен быть числом.')
        continue   

sin_arg = math.radians(degree + seconds / 60)
y = math.sqrt(coef * (math.sin(sin_arg) ** 3)) / (pow_arg ** pow_)
print('y = ', y)

input('Нажмите любую клавишу')
