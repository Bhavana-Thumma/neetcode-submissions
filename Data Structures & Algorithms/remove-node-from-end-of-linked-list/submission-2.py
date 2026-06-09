# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = ListNode()
        dummy = second
        c = 0
        while(first):
            first = first.next
            c+=1
            if(c==n):
                second.next= head
            elif(c>n):
                second = second.next
        second.next = second.next.next
        return dummy.next
        

            
        