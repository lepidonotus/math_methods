import math

print('4302')
print('y = (sin(24degr15sec)*lg(1265))/(62.7^(2/3))')

# y = (sin(24degr15sec)*lg(1265))/(62.7^(2/3))

def root(radicand, sign):
    power = 1 / sign
    return radicand ** power

def main(log_arg, base):

    if log_arg <= 0:
        print('Аргумент логарифма должен быть больше 0')
        return main()
    
    degree = 24
    minutes = 15
    power = 2
    root_sign = 3
    
    angle = degree + minutes / 60
    radians = angle * math.pi / 180 
    sin = math.sin(radians)
    
    log10 = math.log10(log_arg)
    
    numerator = sin * log10
    
    exp = base ** power

    denominator = root(exp, root_sign)
    
    y = numerator / denominator
    
    print('y = ', y)
    print('log_arg = ', log_arg)
    print('pow_base = ', base)
    print('***')

n_str = input('Количество повторов: ')
n = int(n_str)

log_arg_list = []
pow_base_list = []

for i in range(n):
    log_arg = float(input('Аргумент логарифма: '))
    log_arg_list.append(log_arg)

    pow_base = float(input('Основание степени: '))
    pow_base_list.append(pow_base)

    main(log_arg, pow_base)
       

input()