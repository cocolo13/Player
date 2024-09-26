from back import LinkedList
from Composition import Composition
import pygame as pg

pg.mixer.init()


class PlayList(LinkedList):
    def __init__(self, title):
        super().__init__()
        self._title = title
        self._current_track = None

    def play_all(self):
        """Запуск треков
        TODO: доделать обработку исключений"""
        pg.mixer.music.load(self.current_track.data.path)
        pg.mixer.music.play()

    def next_track(self):
        """Go to next track"""
        pg.mixer.music.stop()
        if self.__len__() == 1:
            return self.current_track.data
        return self.current_track.next_item.data

    def previous_track(self):
        """Go to previous track"""
        pg.mixer.music.stop()
        if self.__len__() == 1:
            return self.current_track.data
        return self.current_track.next_item.data

    @property
    def current_track(self):
        return self._current_track

    @current_track.setter
    def current_track(self, value):
        self._current_track = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value