# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return middle_LL(head)

def middle_LL(head):
    if(head == None or head.next == None):
        return head
    temp = head
    length = length_LL(head)
    middle = length//2
    count = 0
    while(count<middle):
        temp = temp.next
        count += 1
    return temp

def length_LL(head):
    temp = head
    count = 0
    while(temp != None):
        temp = temp.next
        count += 1
    return count