# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 600)
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(120, 350, 551, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(340, 480, 90, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        self.pause.setFont(font)
        self.pause.setObjectName("pause")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(170, 480, 121, 100))
        font = QtGui.QFont()
        font.setPointSize(90)
        font.setBold(True)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(480, 480, 121, 100))
        font = QtGui.QFont()
        font.setPointSize(90)
        font.setBold(True)
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.create_playlist = QtWidgets.QPushButton(self.centralwidget)
        self.create_playlist.setGeometry(QtCore.QRect(0, 240, 180, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.create_playlist.setFont(font)
        self.create_playlist.setObjectName("create_playlist")
        self.delete_playlist = QtWidgets.QPushButton(self.centralwidget)
        self.delete_playlist.setGeometry(QtCore.QRect(180, 240, 180, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.delete_playlist.setFont(font)
        self.delete_playlist.setObjectName("delete_playlist")
        self.playlists_list = QtWidgets.QLabel(self.centralwidget)
        self.playlists_list.setGeometry(QtCore.QRect(0, 0, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.playlists_list.setFont(font)
        self.playlists_list.setAlignment(QtCore.Qt.AlignCenter)
        self.playlists_list.setObjectName("playlists_list")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 361, 191))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(420, 50, 361, 191))
        self.listWidget_2.setObjectName("listWidget_2")
        self.playlists_list_2 = QtWidgets.QLabel(self.centralwidget)
        self.playlists_list_2.setGeometry(QtCore.QRect(420, 0, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.playlists_list_2.setFont(font)
        self.playlists_list_2.setAlignment(QtCore.Qt.AlignCenter)
        self.playlists_list_2.setObjectName("playlists_list_2")
        self.create_playlist_2 = QtWidgets.QPushButton(self.centralwidget)
        self.create_playlist_2.setGeometry(QtCore.QRect(420, 250, 180, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.create_playlist_2.setFont(font)
        self.create_playlist_2.setObjectName("create_playlist_2")
        self.delete_playlist_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_playlist_2.setGeometry(QtCore.QRect(600, 250, 180, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.delete_playlist_2.setFont(font)
        self.delete_playlist_2.setObjectName("delete_playlist_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Название трека"))
        self.pause.setText(_translate("MainWindow", "||"))
        self.back.setText(_translate("MainWindow", "<"))
        self.next.setText(_translate("MainWindow", ">"))
        self.create_playlist.setText(_translate("MainWindow", "Добавить"))
        self.delete_playlist.setText(_translate("MainWindow", "Удалить"))
        self.playlists_list.setText(_translate("MainWindow", "Список плейлистов"))
        self.playlists_list_2.setText(_translate("MainWindow", "Список треков"))
        self.create_playlist_2.setText(_translate("MainWindow", "Добавить"))
        self.delete_playlist_2.setText(_translate("MainWindow", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())