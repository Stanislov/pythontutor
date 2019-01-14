''' Суммируем цифры числа, пока не получим одну цифру'''

def digital_root(n):
    while len(str(n))>1:
        z = 0
        for i in str(n):
            z += int(i)
        n = z
    return n

print(digital_root(1234))

''' Лучшие решения:
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):
  return n%9 or n and 9
'''
