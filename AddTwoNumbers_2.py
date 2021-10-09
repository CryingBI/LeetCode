# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def Listprint(self):
        x = self
        while x is not None:
            print(x.val)
            x = x.next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    list = ListNode(0)
    curr = list
    carry = 0
    while(l1 or l2 or carry):
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
            
        curr.next = ListNode(carry%10)
        curr = curr.next
        carry = carry // 10
            
    return list.next


l1 = ListNode(2)
e1 = ListNode(4)
e2 = ListNode(3)
l1.next = e1
e1.next = e2

l2 = ListNode(5)
e3 = ListNode(6)
e4 = ListNode(4)
l2.next = e3
e3.next = e4

l3 = addTwoNumbers(l1,l2)
l3.Listprint()