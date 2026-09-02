import sys
from PySide6 import QtCore, QtWidgets, QtGui

class PromodoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables
        self.timer = self.return_timer()

        self.layout = QtWidgets.QVBoxLayout(self)

        # Layout
        self.layout.addWidget(self.timer)

        self.finish()


    @staticmethod
    def return_timer():
        timer = QtWidgets.QLabel("25:00")
        font = timer.font()
        font.setPixelSize(36)
        font.setBold(True)
        timer.setFont(font)

        return timer

    def timer_start_button(self):
        start_button = QtWidgets.QPushButton("Start")
        start_button.setFixedWidth(100)
        start_button.clicked.connect(self.on_start_button)


    def settings(self):
        ...

    def tasks(self):
        ...

    def popup_button(self):
        ...

    def presets(self):
        ...

    def finish(self):
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    @QtCore.Slot()
    def on_start_button(self):
        self.timer.setText("sometext")