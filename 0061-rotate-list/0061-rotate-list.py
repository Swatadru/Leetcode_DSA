# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None or head.next == None or k==0):
            return head
        length = 0
        temp = head
        while(temp!=None):
            length += 1
            temp= temp.next
        k = k%length
        if k == 0:
            return head
        for i in range(k):
            tail = head
            second_tail = head
            while(tail.next != None):
                tail = tail.next
            while(second_tail.next != tail):
                second_tail = second_tail.next
            tail.next = head
            head = tail
            second_tail.next = None
        return head