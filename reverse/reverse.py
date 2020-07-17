class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is not None:
            # set nextnode as current nodes next
            nextnode = node.next_node
            # overwrite the current nodes next_node as the previous node, reverses
            node.next_node = prev
            # set the current node as previous
            prev = node
            # set the node to the "current nodes" next node
            node = nextnode
            self.reverse_list(node, prev)
        else:
            self.head = prev

# 1->2->3->None
# ```
# would become...
# ```
# 3->2->1->None
