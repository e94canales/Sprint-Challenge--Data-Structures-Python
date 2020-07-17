class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is less than self.value go left
        if value < self.value:
            # if there is no left, put in the node
            if self.left is None:
                self.left = BSTNode(value)
            # otherwise call the childs insert method with the current value
            else:
                self.left.insert(value)
        # otherwise if value is greater than self.value go right
        else:
            # if there is no right, put in the node
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # returns True if target matches the value of the node
        if self.value == target:
            return True
        if target < self.value:
        # if it reaches the end and self.left is None, return False, not in node tree
            if not self.left:
                return False
            return self.left.contains(target) # loop back
        # handle the right side of the tree target > self.value
        else:
            # if self.right is None, return False
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # self.right is None return self.value as the max value
        if not self.right:
            return self.value
        # if self.right is present, run get_max(), runs until it reaches a node with no self.right. All max values are on far right side
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # runs the function on each node
        fn(self.value)

        # # if node has both self.left and self.right, run code for each side
        # if self.left and self.right:
        #     self.left.for_each(fn)
        #     self.right.for_each(fn)

        # if self.left/right is present, run the recursive code
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

