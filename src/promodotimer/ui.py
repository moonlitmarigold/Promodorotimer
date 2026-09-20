from PySide6 import QtCore, QtWidgets, QtGui


class PresetsButton:

    def __init__(self):
        self.background = QtWidgets.QWidget()
        self.background.setStyleSheet("background-color: white;")

        self.layoutVert = QtWidgets.QVBoxLayout()

        self.layoutWork = QtWidgets.QHBoxLayout()

        self.layoutWork.addWidget(QtWidgets.QLabel("Work"))
        self.workLineEdit = QtWidgets.QLineEdit()
        self.layoutWork.addWidget(self.workLineEdit)

        self.layoutPause = QtWidgets.QHBoxLayout()

        self.layoutPause.addWidget(QtWidgets.QLabel("Pause"))
        self.pauseLineEdit = QtWidgets.QLineEdit()
        self.layoutPause.addWidget(self.pauseLineEdit)

        self.confirmButton = QtWidgets.QPushButton("Confirm")
        self.confirmButton.clicked.connect(self.on_confirm_button)

        self.layoutVert.addLayout(self.layoutWork)
        self.layoutVert.addLayout(self.layoutPause)
        self.layoutVert.addWidget(self.confirmButton)

        self.background.setLayout(self.layoutVert)



    @QtCore.Slot()
<<<<<<< Updated upstream
    def OnStartButtonClick(self):
        self.timer.setText("sometext")

class Buttons:

    @staticmethod
    def return_button():
        return None
=======
    def on_confirm_button(self):
        ...
>>>>>>> Stashed changes
