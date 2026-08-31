from PySide6 import QtWidgets,QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(15)

        self.timer = QtWidgets.QLabel("25:00")
        font = self.timer.font()
        font.setPixelSize(36)
        font.setBold(True)
        self.timer.setFont(font)

        startbutton = QtWidgets.QPushButton("Start")
        startbutton.setFixedWidth(100)
        startbutton.clicked.connect(self.OnStartButtonClick)

        layout.addWidget(self.timer)
        layout.addWidget(startbutton)

        centralWiget = QtWidgets.QWidget()
        centralWiget.setLayout(layout)
        self.setCentralWidget(centralWiget)

    @QtCore.Slot()
    def OnStartButtonClick(self):
        self.timer.setText("sometext")