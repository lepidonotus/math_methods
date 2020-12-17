import math
import matplotlib.pyplot as plt

def sin_degree(degree: float, minute: float) -> float:
    return math.sin(math.radians(degree + seconds / 60))

def calculate_expression(pow_arg):
    return math.sqrt(coef * (sin_degree(degree, seconds) ** 3)) / (pow_arg ** pow_)

print('4301 Санников')
print('y = sqrt(7.8 * sin(80deg12min)^3)/(5 ** 0.72)')

# y = sqrt(7.8 * sin(80deg12min)^3)/(5 ** 0.72)

coef = 7.8
# pow_arg = 5

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
        if (seconds < 0) or (seconds > 60):
            print('Секунды должны быть от 0 до 60')
            continue
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

generator1 = [3 + 0.5 * i for i in range(5)]

Y = []
for pow_arg in generator1:
    y = calculate_expression(pow_arg)
    print('pow_arg = ', pow_arg)
    print('y = ', y)
    print('***')
    Y.append(y)

plt.plot(generator1, Y)
plt.show()

input('Нажмите любую клавишу')
