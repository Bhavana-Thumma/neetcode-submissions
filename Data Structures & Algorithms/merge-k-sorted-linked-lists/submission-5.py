# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(a,b):
            dummy = ListNode()
            curr = dummy
            while(a and b):
                if(a.val<=b.val):
                    curr.next = a
                    a= a.next
                else:
                    curr.next=b
                    b=b.next
                curr = curr.next
            curr.next = a or b
            return dummy.next
        def divide(lists, left, right):
            if(left == right):
                return lists[left]
            mid = (left+right) //2
            l1 = divide(lists,left,mid)
            l2 = divide(lists,mid+1, right)
            return merge(l1,l2)
        return divide(lists, 0, len(lists)-1)