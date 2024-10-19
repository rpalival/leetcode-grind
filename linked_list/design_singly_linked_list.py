class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        #dummy node
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        #coz at head we have a dummy sitting
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node
    
    def insertTail(self, val:int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        #traverse and stop at node before the one you want to delete
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
    
    def reverse(self) -> None:
        prev = None
        curr = self.head.next
        while curr:
            fut_next = curr.next
            curr.next = prev
            prev = curr
            curr = fut_next
        self.head.next = prev
    
    def getValues(self) -> list[int]:
        curr = self.head.next
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

myLinkedList = LinkedList()
myLinkedList.insertHead(1)
myLinkedList.insertTail(2)
myLinkedList.insertTail(3)
myLinkedList.insertTail(4)
myLinkedList.remove(2)
myLinkedList.reverse()
print(myLinkedList.getValues())