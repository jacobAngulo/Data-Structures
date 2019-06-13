class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if self.storage[0]:
            return_val = self.storage[0]
            self.storage[0] = self.storage[len(self.storage) - 1]
            # temp = self.storage.pop()
            # self.storage[0] = temp
            self.storage.pop()
            self._sift_down(0)
        return return_val

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if self.storage[(index - 1) // 2]:
            if self.storage[(index - 1) // 2] < self.storage[index]:
                temp = self.storage[index]
                self.storage[index] = self.storage[(index - 1) // 2]
                self.storage[(index - 1) // 2] = temp
                if self.storage[(((index - 1) // 2) - 1) // 2] and self.storage[(((index - 1) // 2) - 1) // 2] < self.storage[(index - 1) // 2]:
                    self._bubble_up((index - 1) // 2)
                else:
                    self._sift_down(index // 2)

    def _sift_down(self, index):
        print(index)
        print((index * 2) + 1)
        print((index * 2) + 2)
        temp = self.storage[index]
        if self.storage[(index * 2) + 1]:
            if self.storage[(index * 2) + 2]:
                if self.storage[(index * 2) + 1] > self.storage[(index * 2) + 2]:
                    if self.storage[(index * 2) + 1] > self.storage[index]:
                        self.storage[index] = self.storage[(index * 2) + 1]
                        self.storage[(index * 2) + 1] = temp
                        self._sift_down((index * 2) + 1)
                elif self.storage[(index * 2) + 2] > self.storage[index]:
                    self.storage[index] = self.storage[(index * 2) + 2]
                    self.storage[(index * 2) + 2] = temp
                    self._sift_down((index * 2) + 2)
            elif self.storage[(index * 2) + 1] > self.storage[index]:
                self.storage[index] = self.storage[(index * 2) + 1]
                self.storage[(index * 2) + 1] = temp
                self._sift_down((index * 2) + 1)
        else:
            pass
