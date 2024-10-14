# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(items: list[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def linkedlist_to_list(head: Optional[ListNode]) -> list[int]:
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items
    
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
    
obj = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
linked_list1_head = list_to_linkedlist(list1)
linked_list2_head = list_to_linkedlist(list2)

reversed_linked_list_head = obj.mergeTwoLists(linked_list1_head, linked_list2_head)
result = linkedlist_to_list(reversed_linked_list_head)
print(result)