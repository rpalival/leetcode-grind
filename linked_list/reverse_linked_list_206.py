# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
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
    
obj = Solution()
head = [1,2,3,4,5]
linked_list_head = list_to_linkedlist(head)
reversed_linked_list_head = obj.reverseList(linked_list_head)
result = linkedlist_to_list(reversed_linked_list_head)
print(result)  # Output should be [5, 4, 3, 2, 1]