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

def deleteDuplicates(head: ListNode) -> ListNode:
        if not head:
            return head
        curr = head
        
        while curr != None and curr.next != None:
            if(curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next
                
            
        return head
        
        
l1 = ListNode(1)
a1 = ListNode(1)     
a2 = ListNode(2) 
a3 = ListNode(3) 
a4 = ListNode(3) 
a5 = ListNode(3) 

l1.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

l2 = deleteDuplicates(l1)
l2.Listprint()
