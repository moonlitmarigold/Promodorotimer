from PySide6 import QtCore, QtWidgets, QtGui
from ..settings import Settings
from .logic import Timer

class TimerUI:

    def __init__(self, main_window:QtWidgets.QMainWindow, settings:Settings):

        self.settings = settings
        self.main_window = main_window

        self.timer_logic = Timer()

        self.timer_logic.set_from_preset(settings.presets.cur_preset)

        self.main_window.timer_label = self.return_timer_label()
        self.main_window.start_button = self.return_timer_start_button()

        self.timer_logic.tick.connect(self.on_tick)
        self.timer_logic.started.connect(self.on_started)
        self.timer_logic.paused.connect(self.on_paused)
        self.timer_logic.finished.connect(self.on_finished)

    def return_timer_label(self):
        timer_label = QtWidgets.QLabel(
            self.format_time(self.timer_logic.start_duration)
        )
        font = timer_label.font()
        font.setPixelSize(36)
        font.setBold(True)
        timer_label.setFont(font)

        return timer_label

    def return_timer_start_button(self):
        start_button = QtWidgets.QPushButton("Start")
        start_button.setFixedWidth(100)
        start_button.clicked.connect(self.on_start_button)

        return start_button


    @staticmethod
    def format_time(seconds: int) -> str:
        return f"{seconds // 60:02d}:{seconds % 60:02d}"

    @QtCore.Slot()
    def on_start_button(self):
        self.timer_logic.toggle()

    @QtCore.Slot(int)
    def on_tick(self, remaining: int):
        self.main_window.timer_label.setText(self.format_time(remaining))

    @QtCore.Slot()
    def on_started(self):
        self.main_window.start_button.setText("Pause")
        self.main_window.timer_label.setText(self.format_time(self.timer_logic.remaining))

    @QtCore.Slot()
    def on_paused(self):
        self.main_window.start_button.setText("Start")

    @QtCore.Slot()
    def on_finished(self):
        self.main_window.start_button.setText("Start")
        self.timer_logic.toggle_break()
        if self.settings.user_settings.auto_start_breaks:
            self.timer_logic.toggle()
        self.main_window.timer_label.setText(self.format_time(self.timer_logic.remaining))