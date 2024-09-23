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

    def create_last(self):
        if self.first_item is None:
            return None
        else:
            last = self.first_item.prev
            return last

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


    def __len__(self):
        if self.first_item is None:
            return 0
        current = self.first_item
        length = 1
        while current.next != self.first_item:
            current = current.next
            length += 1
        return length

def create_linked_list(nodes_list):
    """Создание связного списка"""
    first = previous = None
    for item in nodes_list:
        node = LinkedListItem(item)
        if previous:
            previous.next_item = node
        elif not first:
            first = node
        previous = node
    if previous:
        previous.next_item = first
    return LinkedList(first)

