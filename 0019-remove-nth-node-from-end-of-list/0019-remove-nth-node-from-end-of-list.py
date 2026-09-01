# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head == None:
            return head

        temp = head
        length = 0
        while temp != None:
            temp = temp.next
            length += 1

        index = length - n

        if index == 0:
            return head.next

        temp = head
        count = 0

        while (temp != None and count < index - 1):
            temp = temp.next
            count += 1

        if temp == None or temp.next == None:
            return head

        temp.next = temp.next.next
        return head