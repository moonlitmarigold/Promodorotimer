import sys
from .ui import MainWindow
from PySide6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.showMaximized()
    sys.exit(app.exec())