# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i,node in enumerate(lists):
            if(node):
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        curr = dummy
        while(heap):
            val,i,node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if(curr.next):
                heapq.heappush(heap, (curr.next.val, i, curr.next))
        return dummy.next
# Complexity
# Time: O(N log k)
# Space: O(k)

# ✔ BEST for interviews
# ✔ Most intuitive greedy approach

        