class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
class Solution:
      
    def removeElements(self, head: ListNode, val: int):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next

a7 = ListNode(6)
a6 = ListNode(5, a7)
a5 = ListNode(5, a6)
a4 = ListNode(4, a5)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)


def print_list(node):
    while node:
        print(node.val)
        node = node.next
    print("None")
    
obj = Solution()
new_head = obj.removeElements(a1, 5)
print_list(new_head)