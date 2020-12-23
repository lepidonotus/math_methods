import math

print('4301')
print('y = (sin(24degr15sec)*lg(1265))/(62.7^(2/3))')

# y = (sin(24degr15sec)*lg(1265))/(62.7^(2/3))

def root(radicand, sign):
    power = 1 / sign
    return radicand ** power

def main():
    log_arg_str = input("Аргумент логарифма: ")
    log_arg = float(log_arg_str)

    if log_arg <= 0:
        print('Аргумент логарифма должен быть больше 0')
        return main()
    
    degree = 24
    minutes = 15
    base = 62.7
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
    
    print(y)

main()

input()



