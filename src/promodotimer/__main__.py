import sys
from .app import PromodoWindow
from PySide6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = PromodoWindow()
    widget.showMaximized()
    sys.exit(app.exec())