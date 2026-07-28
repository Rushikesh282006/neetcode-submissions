# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res

        while list1 or list2:

            if list1 == None:
                res.next = ListNode(list2.val)
                res = res.next
                list2 = list2.next
            elif list2 == None:
                res.next = ListNode(list1.val)
                res = res.next
                list1 = list1.next
            elif list1.val == list2.val :
                res.next = ListNode(list1.val)
                res = res.next
                list1 = list1.next
            elif list1.val > list2.val :
                res.next = ListNode(list2.val)
                res = res.next
                list2 = list2.next
            elif list1.val < list2.val :
                res.next = ListNode(list1.val)
                res = res.next
                list1 = list1.next

        return temp.next
