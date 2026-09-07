import sys
from .app import PomodoroWindow
from PySide6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = PomodoroWindow()
    widget.showMaximized()
    sys.exit(app.exec())