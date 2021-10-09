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
def reverseList(head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

l1 = ListNode(1)
e1 = ListNode(2)
e2 = ListNode(3)
e3 = ListNode(4)
e4 = ListNode(5)
l1.next = e1
e1.next = e2
e2.next = e3
e3.next = e4
l2 = reverseList(l1)
l2.Listprint()