# Definition for singly-linked list.
#Solution 1
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
    lenA = 0
    tempA = headA
    while(tempA != None):
        lenA = lenA+1
        tempA = tempA.next
            
    lengthB = 0
    tempB = headB
    while(tempB != None):
        lengthB = lengthB + 1
        tempB = tempB.next
            
    kc = abs(lenA - lengthB)
    tempA = headA
    tempB = headB
    if(lenA > lengthB):
        while(kc>0):
            tempA = tempA.next
            kc = kc - 1
    else: 
        while(kc>0):
            tempB = tempB.next
            kc = kc - 1
    while(tempA != tempB):
        tempA = tempA.next
        tempB = tempB.next
        if(tempA is None or tempB is None):
            return None
        
    return tempA

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
