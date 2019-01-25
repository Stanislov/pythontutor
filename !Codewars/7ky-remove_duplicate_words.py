''' Задается строка, в которой перед выводом убираются повторяющиеся слова'''

''' Самый короткий вариант
def remove_duplicate_words(s):
    return ' '.join(sorted(set(s.split()), key = s.index))

    Или
    return ' '.join(OrderedDict.fromkeys(s.split()))
'''

def remove_duplicate_words(s):
    a = s.split()
    b = [] # создаем пустой список

    # добавляем только уникальные слова
    for i in a:
        if i not in b:
            b.append(i)
    # возвращаем в виде строки
    return ' '.join(b)

    ''' Через множество
    A = set() # создаем пустое множество
    for i in a:
        if i not in A:
            A.add(i)

    peturn(A)
    '''
    '''
    Вариант длиннее, когда убираются повторы внутри самого списка, сначала меняются на ноль, потом удаляются
    k = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] != 0:
                if a[i] == a[j]:
                    a[j]= 0
                    k += 1

    while k != 0:
        a.remove(0)
        k -= 1

    print(a)
    '''

print (remove_duplicate_words("my cat is my cat fat"))
