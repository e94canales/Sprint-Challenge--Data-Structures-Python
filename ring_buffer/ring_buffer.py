class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if self.index is self.capacity:
            self.index = 0

        if len(self.storage) < self.capacity:
            self.storage.append(item)

        else:
            self.storage[self.index] = item
            self.index += 1 % self.capacity


    def get(self):
        return self.storage