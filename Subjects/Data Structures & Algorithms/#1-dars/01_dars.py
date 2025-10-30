'''   
Uyga vazifa
1 . delete by index da tailni marge qilish
2 . length
3 . search(bo'lsa indexsini qaytarish yo'q bo'lsa -1 ni qaytarish) 
'''   

class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next

       
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def delete_front(self):
        self.head = self.head.next
        
    def delete_back(self):
        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None
        self.tail = temp
            
    def prepend(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def traverse(self):
        lst = []
        temp = self.head
        while temp:
            lst.append(temp.value)
            temp = temp.next
        return lst

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        
        new_note = Node(value)
        current = self.head
        while index-1 > 0:
            current = current.next
            index -=1
        new_note.next = current.next
        current.next = new_note
    
    def delete_by_index(self, index):
        if index == 0:
            self.delete_front()
            return
        
        current = self.head
        while index-1 > 0 and current.next:
            current = current.next
            index -=1
        current.next=current.next.next
        
ll = LinkedList()
ll.append(1)            
ll.append(2)            
ll.append(3)
ll.prepend(4)
# ll.delete_front()
# ll.delete_back()
# ll.delete_back()
# ll.delete_back()
ll.insert(0, 18)
print(ll.traverse())            
ll.delete_by_index(4)

print(ll.traverse())            
        
