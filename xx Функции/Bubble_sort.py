# ----------------------------
#
#
# ----------------------------

oldlist = [10, 75, 43, 15, 25, -4, 27]

def bubble_sort(mylist):
    last = len(mylist)-1
    for z in range (0, last):
        for x in range (0, last-z):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist

print ("Oldlist:", oldlist)

newlist = bubble_sort(oldlist).copy()
print("Newlist:", newlist)