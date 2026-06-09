# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(a,b):
            dummy = ListNode()
            curr = dummy
            while(a and b):
                if(a.val<=b.val):
                    curr.next = a
                    a = a.next
                else:
                    curr.next = b
                    b = b.next
                curr = curr.next
            curr.next = a or b
            return dummy.next
        res = None
        for l in lists:
            res = merge(res, l)
        return res