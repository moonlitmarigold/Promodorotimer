import sys
from PySide6 import QtCore, QtWidgets, QtGui

class PromodoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables
        self.timer = self.return_timer()
        self.start_button = self.return_timer_start_button()
        self.settings_button = self.return_settings_button()

        # Layout

        #MainScreen

        # Layout vertical mid
        self.vertical_mid_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_mid_layout.setSpacing(15)

        self.vertical_mid_layout.addStretch()
        self.vertical_mid_layout.addWidget(self.timer, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout.addWidget(self.start_button, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout.addStretch()

        # Layout horizontal_bottom

        self.horizontal_bottom_layout = QtWidgets.QHBoxLayout()
        self.horizontal_bottom_layout.addWidget(self.settings_button)
        self.horizontal_bottom_layout.addStretch()

        self.vertical_mid_layout.addLayout(self.horizontal_bottom_layout)

        #Settings Screen
        self.vertical_mid_layout_set = QtWidgets.QVBoxLayout()
        toggle = QtWidgets.QLabel("This is not a button")
        self.vertical_mid_layout_set.addWidget(toggle)



        #Finish
        self.central_widget = QtWidgets.QStackedWidget()

        self.main_page = QtWidgets.QWidget()
        self.main_page.setLayout(self.vertical_mid_layout)

        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setLayout(self.vertical_mid_layout_set)

        self.central_widget.addWidget(self.main_page)
        self.central_widget.addWidget(self.settings_page)

        self.setCentralWidget(self.central_widget)


    @staticmethod
    def return_timer():
        timer = QtWidgets.QLabel("25:00")
        font = timer.font()
        font.setPixelSize(36)
        font.setBold(True)
        timer.setFont(font)

        return timer


    def return_timer_start_button(self):
        start_button = QtWidgets.QPushButton("Start")
        start_button.setFixedWidth(100)
        start_button.clicked.connect(self.on_start_button)

        return start_button


    def return_settings_button(self):
        settings_button = QtWidgets.QPushButton("Settings")
        settings_button.setFixedWidth(50)
        settings_button.clicked.connect(self.on_settings_button)

        return settings_button

    def tasks(self):
        ...

    def popup_button(self):
        ...


    def presets(self):
        ...


    @QtCore.Slot()
    def on_start_button(self):
        self.timer.setText("6")

    @QtCore.Slot()
    def on_settings_button(self):
        self.central_widget.setCurrentWidget(self.settings_page)