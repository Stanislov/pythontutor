''' Программа для суммирования цифр из заданной строки, проверки на единственное вхождение здесь нет'''

def digits(num):
    s, m = [], []
    for i in str(num):
        s.append(int(i))

    ''' Проводим суммирование ячеек списка'''
    for i in range(len(s)):
        for j in range(len(s)):
            if i<j:
                m.append(s[i]+s[j])

    return m
digits(54321)
