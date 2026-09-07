from PySide6 import QtCore
from .errors import InternalDurationNotSet
from .vars import Preset

class Timer(QtCore.QObject):

    tick = QtCore.Signal(int)  # seconds remaining
    started = QtCore.Signal()
    paused = QtCore.Signal()
    finished = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self._start_duration = None
        self._start_breaK = None
        self._remaining = None
        self.is_break = False

        self._deadline = QtCore.QDeadlineTimer()
        self._ticker = QtCore.QTimer(self)
        self._ticker.setInterval(200)
        self._ticker.setTimerType(QtCore.Qt.TimerType.PreciseTimer)
        self._ticker.timeout.connect(self._on_tick)

    @property
    def start_duration(self):
        if not self._start_duration:
            raise InternalDurationNotSet()

        return self._start_duration

    @property
    def remaining(self):
        if not self._start_duration:
            raise InternalDurationNotSet()

        return self._remaining

    @property
    def is_running(self) -> bool:
        return self._ticker.isActive()

    def toggle(self):
        if not self.is_running:
            self._deadline = QtCore.QDeadlineTimer(self._remaining * 1000)
            self._ticker.start()
            self.started.emit()
        else:
            self._ticker.stop()
            self._remaining = max(0, self._deadline.remainingTime() // 1000)
            self.paused.emit()


    def set_duration_seconds(self, duration:int):
        self._start_duration = duration
        self._remaining = duration

    def set_from_preset(self, p:Preset):
        self._start_duration = p.time_sec
        self._start_breaK = p.pause_time_sec
        self._remaining = self._start_duration
        self.is_break = False

    def reset_to_duration_seconds(self):
        if self.is_running:
            self.toggle()
        self._remaining = self._start_duration

    def _on_tick(self):
        remaining = max(0, -(-self._deadline.remainingTime() // 1000))  # ceil
        if remaining == self.remaining:
            return  # same whole second, nothing to redraw
        self._remaining = remaining
        self.tick.emit(remaining)
        if remaining == 0:
            self._ticker.stop()
            self.finished.emit()

    @staticmethod
    def format_time(seconds: int) -> str:
        return f"{seconds // 60:02d}:{seconds % 60:02d}"