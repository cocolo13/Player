class Composition:
    """Класс трека"""

    def __init__(self, title=None, path=None, length=None):
        """В данном случае name = путь до аудиозаписи"""
        self._title = title
        self._path = path
        self._length = length

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length