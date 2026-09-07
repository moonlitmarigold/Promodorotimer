import sys
from PySide6 import QtCore, QtWidgets, QtGui
from .timer import Timer

class PomodoroWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Variables

        self.timer_logic = self.return_timer_logic()

        self.timer_label = self.return_timer_label()
        self.start_button = self.return_timer_start_button()
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
        preset_2 = QtWidgets.QLabel("megaPreset2")
        preset_3 = QtWidgets.QLabel("megaPreset3")
        preset_4 = QtWidgets.QPushButton("+")


        self.presets_grid.addWidget(preset_1, 0, 0)
        self.presets_grid.addWidget(preset_2, 0, 1)
        self.presets_grid.addWidget(preset_3, 0, 2)
        self.presets_grid.addWidget(preset_4, 1, 1)

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
        task_3 = QtWidgets.QPushButton("+")

        self.vertical_mid_layout_tasks.addStretch()
        self.vertical_mid_layout_tasks.addWidget(tasks_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_tasks.addWidget(task_1, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_tasks.addWidget(task_2, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.vertical_mid_layout_tasks.addWidget(task_3, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
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



    def return_timer_label(self):
        timer_label = QtWidgets.QLabel("25:00")
        font = timer_label.font()
        font.setPixelSize(36)
        font.setBold(True)
        timer_label.setFont(font)

        return timer_label

    def return_timer_logic(self):
        timer_logic = Timer()
        timer_logic.set_duration_seconds( 25 * 60)  # later: from your Preset

        timer_logic.tick.connect(self.on_tick)
        timer_logic.started.connect(self.on_started)
        timer_logic.paused.connect(self.on_paused)
        timer_logic.finished.connect(self.on_finished)

        return timer_logic


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

    @staticmethod
    def format_time(seconds: int) -> str:
        return f"{seconds // 60:02d}:{seconds % 60:02d}"

    @QtCore.Slot()
    def on_start_button(self):
        self.timer_logic.toggle()

    @QtCore.Slot(int)
    def on_tick(self, remaining: int):
        self.timer_label.setText(self.format_time(remaining))

    @QtCore.Slot()
    def on_started(self):
        self.start_button.setText("Pause")
        self.timer_label.setText(self.format_time(self.timer_logic.remaining))

    @QtCore.Slot()
    def on_paused(self):
        self.start_button.setText("Start")

    @QtCore.Slot()
    def on_finished(self):
        self.start_button.setText("Start")
        self.timer_logic.reset_to_duration_seconds()
        self.timer_label.setText(self.format_time(self.timer_logic.remaining))

    @QtCore.Slot()
    def on_settings_button(self):
        self.central_widget.setCurrentWidget(self.settings_page)