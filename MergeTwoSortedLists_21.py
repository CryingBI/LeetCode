class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    def Listprint(self):
        x = self
        while x is not None:
            print(x.val)
            x = x.next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        l3 = dummy
        while (l1 and l2):
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return dummy.next

l1 = ListNode(1)
e2 = ListNode(5)
l1.next = e2
l2 = ListNode(3)
e3 = ListNode(4)
l2.next = e3

l3 = mergeTwoLists(l1,l2)
l3.Listprint()
