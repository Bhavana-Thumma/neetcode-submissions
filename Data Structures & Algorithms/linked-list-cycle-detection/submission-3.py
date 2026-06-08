# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head
        s = dict()
        while(tail):
            if(tail.val in s and s[tail.val] == tail.next):
                return True
            s[tail.val] = tail.next
            tail = tail.next
            print(s.items())
        return False