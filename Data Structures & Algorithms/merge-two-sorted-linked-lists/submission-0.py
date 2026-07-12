# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        one = list1.val
        two = list2.val

        if one <= two:
            return ListNode(one, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(two, self.mergeTwoLists(list1, list2.next))
        