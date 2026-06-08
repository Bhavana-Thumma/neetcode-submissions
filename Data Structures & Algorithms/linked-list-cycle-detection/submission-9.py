# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        tortoise = head
        hare= head.next
        lam = 1
        power =1
        while(hare):
            if(hare == tortoise):
                return True
            if(lam == power):
                tortoise = hare
                power = power*2
                lam = 0
            hare = hare.next
            lam+=1
        return False
# # | Approach                      | Time | Space | Interview Rating     |
# | ----------------------------- | ---- | ----- | -------------------- |
# | Store Visited Nodes (HashSet) | O(n) | O(n)  | Good                 |
# | Floyd's Cycle Detection       | O(n) | O(1)  | Excellent / Expected |
