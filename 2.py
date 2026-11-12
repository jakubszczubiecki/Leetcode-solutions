l1 = [2,4,3]
l2 = [5,6,4]
def addTwoNumbers(l1,l2):
    sl1 = ''
    sl2 = ''
    current = l1
    while current is not None:
        sl1 = str(current.val) + sl1
        current = current.next
    for i in l2:
        sl2 = str(i) + sl2
    tab = [int(i) for i in (str(int(sl1) + int(sl2)))][::-1]
    return tab
print(addTwoNumbers(l1,l2))