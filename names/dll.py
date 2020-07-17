class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def add_to_head(self, value):
        newnode = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            self.length += 1

    def remove_from_head(self): 
        if self.head.next is None:
            current = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return current
        else:
            self.head = self.head.next
            self.length -= 1
            return self.head.value

    def add_to_tail(self, value):
        newnode = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            self.length += 1
        
    def remove_from_tail(self):
        if self.tail.prev is None:
            current = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return current
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

    def move_to_front(self, node):
        if node is self.head:
            return
        elif node is self.tail:
            self.head.prev = node
            self.tail = self.tail.prev
            self.tail.next = None
            node.next = self.head
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            node.next = self.head
            self.head = node

    def move_to_end(self, node):
        if node is self.tail:
            return
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete(self, node):
        if node.next is None and node.prev is None:
            self.head = None
            self.tail = None
            self.length = 0
        if node.next is not None and node.prev is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        if node is self.head:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        if node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
