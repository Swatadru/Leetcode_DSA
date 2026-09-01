# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow != None:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left = head
        right = prev

        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True