"""Модуль узла списка"""


class LinkedListItem:
    """Класс узла списка"""

    def __init__(self, data=None, next=None, prev=None):
        """Конструктор"""
        self.data = data
        self.prev = prev
        self.next = next

    @property
    def next_item(self):
        """Геттер для self._next"""
        return self.next

    @next_item.setter
    def next_item(self, value):
        """Сеттер для self._next"""
        self.next = value
        self.next.prev = self

    @property
    def previous_item(self):
        """Геттер для self._prev"""
        return self.prev

    @previous_item.setter
    def previous_item(self, value):
        """Сеттер для self._prev"""
        self.prev = value
        self.prev.next = self
