import sys
from PySide6 import QtCore, QtWidgets, QtGui
<<<<<<< Updated upstream

from . import settings
from .presets import Preset
from .settings import Settings
from .timer import TimerUI
=======
from .timer import Timer
from .ui import PresetsButton
>>>>>>> Stashed changes

class PomodoroWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables
        self.settings = Settings.load()
        self.timer_ui = TimerUI(self, self.settings)

        self.settings_button = self.return_settings_button()

        # Layout

        # MainScreen

        # Layout horizontal mid
        self.horizontal_mid_layout = QtWidgets.QHBoxLayout()

        # Layout vertical bottom

        self.vertical_bottom_layout_settings = QtWidgets.QVBoxLayout()

        self.vertical_bottom_layout_settings.addStretch()
        self.vertical_bottom_layout_settings.addWidget(self.settings_button)

        self.horizontal_mid_layout.addLayout(self.vertical_bottom_layout_settings)

        # Layout vertical mid
        self.vertical_mid_layout = QtWidgets.QVBoxLayout()
        self.vertical_mid_layout.setSpacing(15)

        self.preset_label = QtWidgets.QLabel("Presets")
         #Presets
        self.presets_grid = QtWidgets.QGridLayout()

        preset_1 = QtWidgets.QLabel("megaPreset1")

        preset_3 = QtWidgets.QLabel("megaPreset3")
        self.preset_button = QtWidgets.QPushButton("+")
        self.preset_button.clicked.connect(self.on_add_preset)


        self.presets_grid.addWidget(preset_1, 0, 0)

        self.presets_grid.addWidget(preset_3, 0, 2)
        self.presets_grid.addWidget(self.preset_button, 1, 1)

        self.vertical_mid_layout.addStretch()
        self.vertical_mid_layout.addWidget(self.timer_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout.addWidget(self.start_button, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout.addWidget(self.preset_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout.addLayout(self.presets_grid)
        self.vertical_mid_layout.addStretch()

        self.horizontal_mid_layout.addStretch(2)
        self.horizontal_mid_layout.addLayout(self.vertical_mid_layout)

        # Layout vertical mid tasks

        self.vertical_mid_layout_tasks = QtWidgets.QVBoxLayout()
        tasks_label = QtWidgets.QLabel("Tasks")


        task_1 = QtWidgets.QLabel("megaTask1")
        task_2 = QtWidgets.QLabel("megaTask2")
        self.task_button = QtWidgets.QPushButton("+")
        self.task_button.clicked.connect(self.on_add_task)

        self.vertical_mid_layout_tasks.addStretch()
        self.vertical_mid_layout_tasks.addWidget(tasks_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_tasks.addWidget(task_1, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_tasks.addWidget(task_2, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_tasks.addWidget(self.task_button, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_tasks.addStretch()

        self.horizontal_mid_layout.addStretch(1)
        self.horizontal_mid_layout.addLayout(self.vertical_mid_layout_tasks)
        self.horizontal_mid_layout.addStretch(1)

        # Settings Screen
        self.vertical_mid_layout_set = QtWidgets.QVBoxLayout()
        toggle = QtWidgets.QLabel("This is not a button", alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_set.addWidget(toggle)

        # Finish
        self.central_widget = QtWidgets.QStackedWidget()

        self.main_page = QtWidgets.QWidget()
        self.main_page.setLayout(self.horizontal_mid_layout)

        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setLayout(self.vertical_mid_layout_set)

        self.central_widget.addWidget(self.main_page)
        self.central_widget.addWidget(self.settings_page)

        self.setCentralWidget(self.central_widget)


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
    def on_settings_button(self):
        self.central_widget.setCurrentWidget(self.settings_page)

    @QtCore.Slot()
    def on_add_task(self):
        ...

    @QtCore.Slot()
    def on_add_preset(self):
        new_pres_button = PresetsButton()
        self.presets_grid.addWidget(new_pres_button.background, 0, 1)

