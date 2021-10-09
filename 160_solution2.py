# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def Listprint(self):
        x = self
        while x is not None:
            print(x.val)
            x = x.next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
        tempA = headA
        tempB = headB
        while(tempA!= tempB):
            if(tempA != None):
                tempA = tempA.next
            else:
                tempA = headB
            if(tempB != None):
                tempB = tempB.next
            else:
                tempB = headA
        
        return tempA

#doan code vong while viet gon trong C hoac Java
""" while(tempA != tempB){
            tempA = tempA != null ? tempA.next : headB;
            tempB = tempB != null ? tempB.next : headA;
        }"""
# link: youtube.com/watch?v=8qi8a2ph71o

l1 = ListNode(1)
e1 = ListNode(9)
e2 = ListNode(1)
e3 = ListNode(2)
e4 = ListNode(4)
l1.next = e1
e1.next = e2
e2.next = e3
e3.next = e4

l2 = ListNode(3)

l2.next = e3

l3 = getIntersectionNode(l1,l2)
l3.Listprint()
