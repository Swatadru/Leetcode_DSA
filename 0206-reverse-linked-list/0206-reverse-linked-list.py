# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return reverse(head)

def reverse(head):
    if(head == None or head.next == None):
        return head
    ans = reverse(head.next)
    head.next.next = head
    head.next = None
    return ans