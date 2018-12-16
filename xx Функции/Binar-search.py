def binar(mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == mylist[0]:
            return "0"
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binar(mylist, iskat, start, mid - 1)
        else:
            return binar(mylist, iskat, mid + 1, stop)

mylist=[10, 12, 13, 15, 20, 24, 27, 33, 40, 51, 57, 68, 70, 77, 79, 81, 85, 88, 91, 95, 99]
iskat = 10
start = 0
stop = len(mylist)

x = binar(mylist, iskat, start, stop)

if x == False:
    print("Элемент", iskat, "не найден в массиве")
else:
    print("Элемент", iskat, "в массиве находится на позиции", x)