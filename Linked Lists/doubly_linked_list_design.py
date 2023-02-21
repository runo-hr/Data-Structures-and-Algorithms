# Definition for doubly-linked list.
class ListNode:
     def __init__(self, x=None):
         self.val = x
         self.next = None
         self.prev = None
    
class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.len = 0

    def get(self, index: int) -> int:
        curr = self.left.next
        counter = 0
        for i in range(index):
            if curr.next != self.right:
                curr = curr.next
                counter += 1
            else:
                break
        if counter == index and self.len != 0:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.left, self.left.next
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.left.next
        counter = 0
        for i in range(index):
            if next.next:
                next = next.next
                counter += 1
            else:
                break
        if counter == index:
            node, prev = ListNode(val), next.prev
            node.next, node.prev = next, prev
            next.prev = node
            prev.next = node
            self.len += 1


    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next
        counter = 0
        for i in range(index):
            if node.next != self.right:
                node = node.next
                counter += 1
            else:
                break
        if counter == index and self.len != 0:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.len -= 1

       
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
obj = MyLinkedList()
obj.addAtHead(2)
obj.deleteAtIndex(1)

obj.addAtHead(2)
obj.addAtHead(7)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(5)

obj.addAtTail(5)
print(obj.get(5))

obj.deleteAtIndex(6)
obj.deleteAtIndex(4)

#obj.addAtIndex(0,10)
#obj.addAtIndex(0,20)
#obj.addAtIndex(1,30)
#print(obj.get(0))
#obj.deleteAtIndex(0)
#print(obj.get(0))