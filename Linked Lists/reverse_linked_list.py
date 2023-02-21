# Definition for singly-linked list.
for i in range(0):
    print(f'i : {i}')
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
heda = ListNode(5)
heda.next= ListNode(4)
heda.next.next = ListNode(3)
# print(heda.next.next.val)

class Solution:
    def reverse_pointers(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverse_recursively(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        new_head = head
        # print(f'new_head : {new_head.val}')
        if head.next:
            new_head = self.reverse_recursively(head.next)
            # print(f'new_head : {new_head.val}')
            # print(f'head : {head.val}')
            # print(f'head.next : {head.next.val}')
            head.next.next = head # reverse
        # print(f'head : {head.val}')
        head.next = None
        # print(f'new_head : {new_head.val}')
        return new_head

solver = Solution()
print(f'heda : {heda.val}')
new_heda = solver.reverse_recursively(heda) 
print(f'new_heda : {new_heda.val}')
new_heda2 = solver.reverse_pointers(new_heda) 
print(f'new_heda2: {new_heda2.val}')