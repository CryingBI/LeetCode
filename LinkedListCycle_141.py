# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while(fast!=None and fast.next != None):
        fast = fast.next.next
        slow = slow.next
        if(slow == fast):
            return True
        
    return False

a = ListNode(3)
b = ListNode(0)
c = ListNode(1)
a.next =b
b.next =c


s = hasCycle(a)
print(s)