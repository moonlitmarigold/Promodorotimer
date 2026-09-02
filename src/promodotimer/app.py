import sys
from PySide6 import QtCore, QtWidgets, QtGui

class PromodoWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("67")
        self.text = QtWidgets.QLabel("1984", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.timer()

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText('Hello')

    def timer(self):
        self.timer = QtWidgets.QLabel("25:00")
        font = self.timer.font()
        font.setPixelSize(36)
        font.setBold(True)
        self.timer.setFont(font)

    def settings(self):
        ...

    def tasks(self):
        ...

    def popup_button(self):
        ...

    def presets(self):
        ...