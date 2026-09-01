# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sorted_list(list1,list2)

def merge_sorted_list(head1,head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    finalHead = None
    finalTail = None
    while(head1 != None and head2 != None):
        if(head1.val<head2.val):
            if(finalHead == None):
                finalHead = head1
                finalTail = head1
            else:
                finalTail.next = head1
                finalTail = head1
            head1 = head1.next
        else:
            if(head2.val<=head1.val):
                if(finalHead == None):
                    finalHead = head2
                    finalTail = head2
                else:
                    finalTail.next = head2
                    finalTail = head2
                head2 = head2.next
    
    if(head1 != None):
        finalTail.next = head1
    if(head2 != None):
        finalTail.next = head2
    
    return finalHead