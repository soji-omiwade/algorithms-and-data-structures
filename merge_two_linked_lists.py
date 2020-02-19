class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
        
    def __str__(self):
        v=self
        while v is not None:
            print(v.val)
            v=v.next
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
l1=ListNode(2,ListNode(4))
l2=ListNode(1,ListNode(3))
print(Solution().mergeTwoLists(l1,l2))