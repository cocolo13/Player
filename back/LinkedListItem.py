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
