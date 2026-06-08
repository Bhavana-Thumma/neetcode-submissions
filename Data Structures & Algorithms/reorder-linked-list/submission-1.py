# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while(curr):
            nxt = curr.next
            curr.next=prev
            prev = curr
            curr = nxt
        curr,tail = head,prev
        while(tail):
            temp1 = curr.next
            temp2 = tail.next
            curr.next = tail
            tail.next = temp1
            curr = temp1
            tail =temp2
        


            
        


