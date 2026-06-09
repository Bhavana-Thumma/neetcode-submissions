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
        window = 1
        n = len(lists)
        while(window<n):
            for i in range(0, n-window, window*2):
                lists[i] = merge(lists[i], lists[i+window])
            window*=2
        return lists[0] if lists else None
        