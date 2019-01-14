''' Мы меняем прописные и строчные буквы на цифры '''
''' test.assert_equals(alphabet_position("The narwhal bacons at midnight."),
    "20(t) 8(h) 5(e) 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")'''

def alphabet_position(text):
    b = str(text)
    c = []
    k = 0

    for i in range(len(b)):
        c.append(str(b[i]))

    # проверка, что данные приняты
    # print(c)
    # print('Длинна:', len(c))

    Spisok = ['A', 'a','B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    s = [['A', 'a', 1], ['B', 'b', 2], ['C', 'c', 3], ['D', 'd', 4], ['E', 'e', 5], ['F', 'f', 6], ['G', 'g', 7], ['H', 'h', 8], ['I', 'i', 9], ['J', 'j', 10], ['K', 'k', 11], ['L', 'l', 12], ['M', 'm', 13], ['N', 'n', 14], ['O', 'o', 15], ['P', 'p', 16], ['Q', 'q', 17], ['R', 'r', 18], ['S', 's', 19], ['T', 't', 20], ['U', 'u', 21], ['V', 'v', 22], ['W', 'w', 23], ['X', 'x', 24], ['Y', 'y', 25], ['Z', 'z', 26] ]

    # циклы на проверку наличия букв в списке
    for i in range(len(c)):
        # print (c[i])
        if c[i] in Spisok:
            for j in range(len(s)):
                # print ('i,j=', i, j, 'c[i]=', c[i], 's[j]=', s[j])
                if str(c[i]) == s[j][0] or c[i] == s[j][1]:
                    # print (c[i], ' - ', s[j][0], 'or', s[j][1], 'Заменяем!')
                    c[i] = s[j][2]
        else:
            # print(c[i], "- не найдено пары, удаляем")
            # c.pop(i)
            # если буквы нет в списке, то меняем её на ноль
            c[i] = 0
            k += 1

    # цикл на удаление лишних знаков, здесь это "0"
    while k != 0:
        c.remove(0)
        k -= 1

    # возвращаем или печатаем список через пробел
    return(' '.join([str(i) for i in c]))
    # print(c)





alphabet_position("The sunset o' clock.")
