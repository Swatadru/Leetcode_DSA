# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        new_l1 = int("".join(str(x) for x in list1)[::-1])
        new_l2 = int("".join(str(x) for x in list2)[::-1])
        total = new_l1 + new_l2
        dummy = curr = ListNode(0)
        for digit in str(total)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next