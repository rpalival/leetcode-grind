class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        #dummy head and tail
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1
    
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        prev = self.head
        next = self.head.next

        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        prev = self.tail.prev
        next = self.tail

        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and index == 0:
            node = ListNode(val)
            prev = cur.prev
            next = cur

            node.next = next
            node.prev = prev
            next.prev = node
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1
        
        if cur and cur != self.tail and index == 0:
            prev = cur.prev
            next = cur.next

            next.prev = prev
            prev.next = next

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(3)
myLinkedList.addAtTail(4)
myLinkedList.addAtTail(5)
myLinkedList.addAtTail(6)