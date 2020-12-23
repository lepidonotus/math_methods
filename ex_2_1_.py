import math

print('4301')
print('y = (sin(24degr15sec)*lg(1265))/(62.7^(2/3))')

# y = (sin(24degr15sec)*lg(1265))/(62.7^(2/3))

log_arg_str = input("Аргумент логарифма: ")
log_arg = float(log_arg_str)

degree = 24
minutes = 15
#log_arg = 1265
base = 62.7
power = 2 / 3

angle = degree + minutes / 60
# с math.pi результат намного точнее, чем с 3.14
radians = angle * math.pi / 180 
sin = math.sin(radians)

log10 = math.log10(log_arg)

numerator = sin * log10

exp = base ** power

y = numerator / exp

print(y)

input()



