import sys

from PyQt5 import uic
import pygame
from PyQt5.QtCore import QTimer
from pygame import mixer

from back.Composition import Composition
from playList import PlayList
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, \
    QDialog, QTextEdit, QDialogButtonBox, QListWidget, QListWidgetItem, \
    QLineEdit, QLabel, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.all_playlist = list()
        self.current_playlist: None | PlayList = None
        # Загружаем ui макет стартового окна и устанавливаем иконку приложения
        uic.loadUi("front/window1.ui", self)
        mixer.init()

        # Timer
        self.pause = None
        self.timer = QTimer()
        self.remaining_time = 0
        self.timer.timeout.connect(self.play_next_track)

        self.title_track = self.findChild(QLabel, "titletrack")
        ...

        self.playlists_list = self.findChild(QListWidget, "listplaylist")
        self.playlists_list.itemClicked.connect(self.set_current_playlist)

        self.list_track = self.findChild(QListWidget, "listtrack")
        self.list_track.itemClicked.connect(self.set_current_track)  ###

        self.btn_add_playlist = self.findChild(QPushButton, "addplaylist")
        self.btn_add_playlist.clicked.connect(self.create_playlist)

        self.btn_del_playlist = self.findChild(QPushButton, "delplaylist")
        self.btn_del_playlist.clicked.connect(self.delete_playlist)

        self.btn_add_track = self.findChild(QPushButton, "addtrack")
        self.btn_add_track.clicked.connect(self.add_track)

        self.btn_del_track = self.findChild(QPushButton, "deltrack")
        self.btn_del_track.clicked.connect(self.delete_track)

        self.pause = self.findChild(QPushButton, "pause")
        self.pause.clicked.connect(self.play)

        self.next_track = self.findChild(QPushButton, "next")
        self.next_track.clicked.connect(self.play_next_track)

        self.previous_track = self.findChild(QPushButton, "back")
        self.previous_track.clicked.connect(self.play_prev_track)

        self.btn_move = self.findChild(QPushButton, "move")
        self.btn_move.clicked.connect(self.move_track)

    def create_playlist(self):
        """Метод для создания нового плейлиста через диалоговое окно."""
        dialog = Window2()
        if dialog.exec_() == QDialog.Accepted:
            playlist_title = dialog.playlist_title_edit.toPlainText().strip()
            playlist_title = playlist_title.replace("\t", " ").replace("\n", " ")
            if not all(p.title != playlist_title for p in self.all_playlist):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Ошибка")
                msg.setInformativeText('Плейлист с таким названием уже существует')
                msg.setWindowTitle("Ошибка")
                msg.exec_()
            if playlist_title:
                self.all_playlist.append(PlayList(playlist_title))
                self.playlists_list.addItem(playlist_title)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Ошибка")
                msg.setInformativeText('Название не может быть пустым')
                msg.setWindowTitle("Ошибка")
                msg.exec_()

    def set_current_playlist(self, playlist_title):
        """обработка нажатия на плейлист (некоторый)"""
        mixer.music.stop()
        self.pause = None
        self.timer.stop()
        self.remaining_time = 0
        for playlist in self.all_playlist:
            if playlist.title == playlist_title.text():
                if self.current_playlist:
                    # self.title_track.setText("Title") # исправить, чтобыа менялось название плейлиста а не трека
                    self.current_playlist.current_track = None
                self.current_playlist = playlist
                self.list_track.clear()
                for track in self.current_playlist:
                    self.list_track.addItem(QListWidgetItem(track.data.title))

    def add_track(self):
        # mixer.music.stop()
        # self.pause = None
        # self.timer.stop()
        # self.remaining_time = 0
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ошибка")
        # msg.setInformativeText('Сначала необходимо создать плейлист')
        msg.setWindowTitle("Ошибка")

        if len(self.all_playlist) == 0:
            msg.setInformativeText('Сначала необходимо создать плейлист')
            msg.exec_()
        elif self.current_playlist is None:
            msg.setInformativeText('Выберите плейлист, в который хотите добавить трек')
            msg.exec_()
        else:
            window3 = Window3()
            if window3.exec_() == QDialog.Accepted:
                track_title = window3.track_title.toPlainText().strip()
                # track_title = track_title.replace("\t", " ").replace("\n", " ")
                track_path = window3.path.text()
                if not track_path or not track_title.replace(" ", ""):
                    msg.setInformativeText('Все поля должны быть заполнены')
                    msg.exec_()
                    return
                for track in self.current_playlist:
                    if track.data.title == track_title:
                        msg.setInformativeText('Трек с таким названием уже есть в плейлисте')
                        msg.exec_()
                        return
                try:
                    track_length = mixer.Sound(track_path).get_length()
                except (FileNotFoundError, pygame.error):
                    msg.setInformativeText('Данные файл не поддерживается')
                    msg.exec_()
                    return
                composition = Composition(title=track_title, path=track_path, length=track_length)
                track_item = QListWidgetItem(f"{composition.title}")
                self.current_playlist.append(composition)  # add iter!! in LinkedList
                self.list_track.addItem(track_item)

    def set_current_track(self, track: QListWidgetItem):
        mixer.music.stop()
        self.pause = None
        self.timer.stop()
        self.remaining_time = 0
        for t in self.current_playlist:
            if t.data.title == track.text():
                self.current_playlist.current_track = t
                self.title_track.setText(t.data.title)
                return

    def play(self):
        "Play current track"
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ошибка")
        # msg.setInformativeText('Сначала необходимо создать плейлист')
        msg.setWindowTitle("Ошибка")
        if len(self.all_playlist) == 0:
            msg.setInformativeText('Список плейлистов пуст')
            msg.exec_()
            return
        if not self.current_playlist:
            msg.setInformativeText('Текущий плейлист пуст')
            msg.exec_()
            return
        if not self.current_playlist.current_track:
            msg.setInformativeText('Выберите трек из списка')
            msg.exec_()
            return
        if (self.current_playlist is not None and
                self.current_playlist.current_track is not None):
            if self.pause is None:
                self.current_playlist.play_all()
                self.timer.start(int(self.current_playlist.current_track.data.length * 1000))
                self.pause = False
            elif self.pause:
                mixer.music.unpause()
                self.timer.start(self.remaining_time)
                self.pause = False
            else:
                mixer.music.pause()
                self.remaining_time = self.timer.remainingTime()
                self.timer.stop()
                self.pause = True

    def play_next_track(self):
        if ((self.current_playlist is not None) and
                (self.current_playlist.current_track is not None)):
            self.current_playlist.current_track = self.current_playlist.current_track.next
            self.current_playlist.play_all()
            self.timer.stop()
            self.remaining_time = 0
            self.timer.start(int(self.current_playlist.current_track.data.length * 1000))
            self.pause = False
            self.title_track.setText(self.current_playlist.current_track.data.title)

    def play_prev_track(self):
        if ((self.current_playlist is not None) and
                (self.current_playlist.current_track is not None)):
            self.current_playlist.current_track = (
                self.current_playlist.current_track.previous_item)
            self.current_playlist.play_all()
            self.timer.stop()
            self.remaining_time = 0
            self.timer.start(int(self.current_playlist.current_track.data.length * 1000))
            self.pause = False
            self.title_track.setText(self.current_playlist.current_track.data.title)
            # self.author_label.setText(self.current_playlist.current_track.data.author)

    def delete_track(self):
        """Function for delete track"""
        mixer.music.stop()
        self.pause = None
        self.timer.stop()
        self.remaining_time = 0
        self.title_track.setText("")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ошибка")
        if len(self.all_playlist) == 0:
            msg.setInformativeText('К сожалению, Вам нечего удалять')
            msg.exec_()
            return
        if self.current_playlist is None:
            msg.setInformativeText('Пожалуйста, выберите плейлист')
            msg.exec_()
            return
        if self.current_playlist.current_track is None and self.current_playlist is not None:
            msg.setInformativeText('Пожалуйста, выберите трек, который хотите удалить')
            msg.exec_()
            return
        if (self.current_playlist is not None
                and self.current_playlist.current_track is not None):
            track_item = self.list_track.selectedItems()[0]
            self.list_track.takeItem(
                self.list_track.row(track_item))
            for i in self.current_playlist:
                if i.data.title == track_item.text():
                    self.current_playlist.remove(i.data)
                    self.current_playlist.current_track = None
                    return

    def delete_playlist(self):
        """Function for delete playlist"""
        mixer.music.stop()
        self.pause = None
        self.timer.stop()
        self.remaining_time = 0
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ошибка")
        if len(self.all_playlist) == 0:
            msg.setInformativeText('К сожалению, Вам нечего удалять')
            msg.exec_()
            return
        if self.current_playlist is None:
            msg.setInformativeText('Пожалуста, выберите плейлист, который хотите удалить')
            msg.exec_()
            return
        else:
            self.list_track.clear()
            self.all_playlist.remove(self.current_playlist)
            playlist_item = self.playlists_list.selectedItems()[0]
            self.playlists_list.takeItem(self.playlists_list.row(playlist_item))
            self.current_playlist = None
            self.title_track.setText("")

    def move_track(self):
        mixer.music.stop()
        self.music_paused = None
        self.timer.stop()
        self.remaining_time = 0
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ошибка")
        if len(self.all_playlist) == 0:
            msg.setInformativeText('Сначала необходимо создать плейлист')
            msg.exec_()
            return
        if self.current_playlist is None:
            msg.setInformativeText('Пожалуста, выберите плейлист')
            msg.exec_()
            return
        if len(self.current_playlist) < 2:
            msg.setInformativeText('В плейлисте должно быть минимум два трека')
            msg.exec_()
            return
        window4 = Window4()
        window4.f_index.setMaximum(len(self.current_playlist))
        window4.s_index.setMaximum(len(self.current_playlist))
        if window4.exec_() == QDialog.Accepted:
            first = window4.f_index.value() - 1
            second = window4.s_index.value() - 1
            if first == second:
                msg.setInformativeText('Пожалуста, выберите два разных индекса')
                msg.exec_()
                return
            remove = self.current_playlist[first]
            if second == len(self.current_playlist)-1 and first == 0:
                ins = self.current_playlist[second]
                self.current_playlist.remove(self.current_playlist[second])
                self.current_playlist.append_left(ins)
            elif second == -1:
                self.current_playlist.remove(remove)
                self.current_playlist.append_left(remove)
            else:
                prev = self.current_playlist[second]
                self.current_playlist.remove(remove)
                self.current_playlist.insert(prev, remove)
            self.list_track.clear()
            for track in self.current_playlist:
                self.list_track.addItem(QListWidgetItem(track.data.title))
            self.current_playlist.current_track = None
            self.title_track.setText("")
        return


class Window2(QDialog):
    """Окно для создания плейлиста
    Вводится название плейлиста и сохраняется
    input"""

    def __init__(self):
        super().__init__()
        uic.loadUi("front/window2.ui", self)
        # Находим виджеты в загруженном интерфейсе
        self.playlist_title_edit = self.findChild(QTextEdit, 'input_title')
        self.buttons_box = self.findChild(QDialogButtonBox, 'buttonBox')

        # Связываем кнопки с методами
        self.buttons_box.accepted.connect(self.accept)  # Закрытие окна с подтверждением
        self.buttons_box.rejected.connect(self.reject)  # Закрытие окна с отменой


class Window3(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("front/window3.ui", self)
        self.track_title = self.findChild(QTextEdit, "input_title")
        self.path_btn = self.findChild(QPushButton, "btn")
        self.buttons_box = self.findChild(QDialogButtonBox, "buttonBox")
        self.path = self.findChild(QLineEdit, "lineEdit")
        self.buttons_box.accepted.connect(self.accept)  # Закрытие окна с подтверждением
        self.buttons_box.rejected.connect(self.reject)

        self.path_btn.clicked.connect(self.select_file)

    def select_file(self):
        """Метод для открытия диалогового окна с выбором файла и последующим выбором"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "", "",
                                                   "Audio Files (*.mp3)", options=options)
        if file_name:
            self.path.setText(file_name)


class Window4(QDialog):
    def __init__(self):
        """Конструктор"""
        super().__init__()
        uic.loadUi("front/window4.ui", self)
        self.f_index = self.findChild(QSpinBox, "first_index")
        self.s_index = self.findChild(QSpinBox, "second_index")
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        self.buttonBox.accepted.connect(self.accept)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
