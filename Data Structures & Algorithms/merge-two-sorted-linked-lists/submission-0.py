# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while(list1 and list2):
            if(list1.val <=list2.val):
                arr.append(list1.val)
                list1=list1.next
            else:
                arr.append(list2.val)
                list2=list2.next
        while(list1):
            arr.append(list1.val)
            list1 = list1.next
        while(list2):
            arr.append(list2.val)
            list2 = list2.next
        arr.sort()
        print(arr)
        dummy = ListNode(0)
        head = dummy
        for num in arr:
            head.next = ListNode(num)
            head = head.next
        return dummy.next
            






