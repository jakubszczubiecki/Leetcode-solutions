# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        sl1 = ''
        sl2 = ''
        current = l1
        while current is not None:
            sl1 = str(current.val) + sl1
            current = current.next
        current = l2
        while current is not None:
            sl2 = str(current.val) + sl2
            current = current.next
        tab = [int(i) for i in (str(int(sl1) + int(sl2)))][::-1]
        head = ListNode(tab[0])
        current = head
        for i in range(1, len(tab)):
            current.next = ListNode(tab[i])
            current = current.next
        return head