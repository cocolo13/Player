class LinkedListItem:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

    @property
    def next_item(self):
        return self.next

    @next_item.setter
    def next_item(self, value):
        self.next = value
        self.next.prev = self

    @property
    def previous_item(self):
        return self.prev

    @previous_item.setter
    def previous_item(self, value):
        self.prev = value
        self.prev.next = self


class LinkedList:
    def __init__(self, first_item=None):
        self.first_item = first_item
        self.last = self.create_last()
        self.iter_value = 0
        self.value = None

    def create_last(self):
        if self.first_item is None:
            return None
        else:
            last = self.first_item.prev
            return last

    def search_elem(self, elem):
        if self.first_item is None:
            return False
        current = self.first_item
        while current.next != self.first_item:
            if current == elem:
                return True
            current = current.next
        return current == elem

    def append_right(self, item):
        new_node = LinkedListItem(item)
        if self.first_item is None:  # 0
            self.first_item = new_node
            self.first_item.next = new_node
            self.first_item.prev = new_node
            self.last = new_node
            return
        if self.first_item == self.first_item.next:  # 1
            self.last = new_node
            self.last.prev = self.first_item
            self.last.next = self.first_item
            self.first_item.prev = self.last
            self.first_item.next = self.last
            return
        self.last.next = new_node
        new_node.next = self.first_item
        new_node.prev = self.last
        self.first_item.prev = new_node
        self.last = new_node

    def append(self, item):
        new_node = LinkedListItem(item)
        if self.first_item is None:
            self.first_item = new_node
            self.first_item.next = new_node
            self.first_item.prev = new_node
            self.last = new_node
            return
        if self.first_item == self.first_item.next:
            self.last = new_node
            self.last.prev = self.first_item
            self.last.next = self.first_item
            self.first_item.prev = self.last
            self.first_item.next = self.last
            return
        self.last.next = new_node
        new_node.next = self.first_item
        new_node.prev = self.last
        self.first_item.prev = new_node
        self.last = new_node

    def append_left(self, item):
        new_node = LinkedListItem(item)
        if self.first_item is None:
            self.first_item = new_node
            self.last = new_node
            self.first_item.next = new_node
            self.first_item.prev = new_node
            self.last.next = new_node
            self.last.prev = new_node
            return
        if self.first_item.next == self.first_item:
            new_node.next = self.last
            new_node.prev = self.last
            self.first_item = new_node
            self.last.prev = new_node
            self.last.next = new_node
            return
        self.last.next = new_node
        self.first_item.prev = new_node
        new_node.next = self.first_item
        new_node.prev = self.last
        self.first_item = new_node

    def __contains__(self, item):
        if self.first_item is None:
            return False
        current = self.first_item
        if current.next == self.first_item:
            return current.data == item
        while current.next != self.first_item:
            if current.data == item:
                return True
            current = current.next
        return current.data == item

    def __getitem__(self, item):
        length = self.__len__()
        if item >= 0:
            if length - 1 < item or length == 0:
                raise IndexError
            i = 0
            current = self.first_item
            while i != item:
                current = current.next
                i += 1
        else:
            if -1 * length > item:
                raise IndexError
            current = self.first_item
            i = -1 * length
            while i != item:
                current = current.prev
                i += 1
        return current.data

    def insert(self, previous, item):
        """Работает, только если в тесте убрать .data"""
        new_node = LinkedListItem(item)
        current = self.first_item
        while current.data != previous:
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        new_node.next.prev = new_node

    def __str__(self):
        string = ""
        if self.first_item is None:
            return string
        current = self.first_item
        while current.next != self.first_item:
            string += str(current.data) + " "
            current = current.next
        string += str(current.data) + " "
        return string[:-1]

    def remove(self, item):
        if not self.__contains__(item):
            raise ValueError
        if self.__len__() == 1:
            self.first_item = None
            self.last = None
            return
        if self.__len__() >= 2:
            if item == self.first_item.data:
                first = self.first_item.next
                self.first_item = first
                self.first_item.prev = self.last
                self.last.next = first
                return
            if item == self.last.data:
                last = self.last.prev
                self.last = last
                self.last.next = self.first_item
                return
            current = self.first_item
            while current.data != item:
                current = current.next
            prev = current.prev
            next = current.next
            current.next.prev = prev
            current.prev.next = next

    def __len__(self):
        if self.first_item is None:
            return 0
        current = self.first_item
        length = 1
        while current.next != self.first_item:
            current = current.next
            length += 1
        return length

    def __iter__(self):
        self.value = self.first_item
        self.iter_value = 0
        return self

    def __next__(self):
        if self.first_item is None:
            raise StopIteration
        if self.__len__() <= self.iter_value:
            raise StopIteration
        item = self.value
        self.value = self.value.next_item
        self.iter_value += 1
        return item

