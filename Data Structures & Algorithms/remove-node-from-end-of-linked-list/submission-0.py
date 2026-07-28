# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        len_list = 0

        while temp:
            temp = temp.next
            len_list += 1
        
        if len_list == n:
            return head.next

        temp = head

        for _ in range(len_list - n - 1):
            temp = temp.next
        
        temp_two = temp.next
        temp.next = temp_two.next

        return head