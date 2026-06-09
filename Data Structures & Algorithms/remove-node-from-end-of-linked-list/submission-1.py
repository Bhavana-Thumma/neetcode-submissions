# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr =[]
        curr = head
        while(curr):
            arr.append(curr)
            curr = curr.next
        N = len(arr)
        dummy = ListNode()
        c = dummy
        for i in range(N):
            if(i == (N-n)):
                continue
            print(i)
            c.next = arr[i]
            c = c.next
        c.next = None
        return dummy.next
        