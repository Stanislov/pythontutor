''' Функция, которая берет строку с числами и взвращает строку с квадратами этих чисел '''
# Лучшее решение. https://www.codewars.com/kata/square-every-digit/solutions/python
# def square_digits(num):
#    return int(''.join(str(int(d)**2) for d in str(num)))

def square_digits(num):
    b = str(num)
    c = []

    for i in range(len(b)):
        c.append(b[i])
        c[i] = int(c[i])*int(c[i])

    a = ''.join([str(i) for i in c])
    a = int(a)
    return a

print(square_digits(9119))
