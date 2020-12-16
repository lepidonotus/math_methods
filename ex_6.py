import math
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def sin_degree(degree, minute):
    return math.sin(math.radians(degree + seconds / 60))

def calculate_expression(degree, pow_arg):
    return math.sqrt(coef * (sin_degree(degree, seconds) ** 3)) / (pow_arg ** pow_)

print('4301 Санников')
print('y = sqrt(7.8 * sin(80deg12min)^3)/(5 ** 0.72)')

# y = sqrt(7.8 * sin(80deg12min)^3)/(5 ** 0.72)

coef = 7.8  

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

while True:
    try:
        repeats = int(input('Количество повторов: '))
        if repeats < 0:
            print('Количество повторов должно быть положительным')
            continue
        break
    except:
        print ('Количество повторов должно быть целым числом.')
        continue   

A = []
B = []

for i in range(repeats):
    while True:
        try:
            a = float(input('Градусы a: '))
            break
        except:
            print ('Градусы должны быть числом.')
            continue
    A.append(a)
    while True:
        try:
            b = float(input('Основание степени b: '))
            break
        except:
            print ('Основание степени должно быть числом.')
            continue
    B.append(b)

z = []
for pow_arg in A:
    row = []
    for degree in B:
        y = calculate_expression(degree, pow_arg)
        print(y)
        row.append(y)
    z.append(row)

Z = np.array(z)
print(Z.ndim)

X, Y = np.meshgrid(B, A)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()


input('Нажмите любую клавишу')
