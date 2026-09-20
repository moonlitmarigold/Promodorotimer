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


class EditableLabel(QtWidgets.QLineEdit):
    """Renders as a label; double-click turns it into a real line edit."""

    def __init__(self, text: str, on_commit, parent=None):
        super().__init__(text, parent)

        self._on_commit = on_commit
        self._before = text

        self._stop_edit()
        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.editingFinished.connect(self._commit)

    def mouseDoubleClickEvent(self, event):
        if self.isReadOnly():
            self._start_edit()
        else:
            super().mouseDoubleClickEvent(event)

    def keyPressEvent(self, event):
        if not self.isReadOnly() and event.key() == QtCore.Qt.Key.Key_Escape:
            self.setText(self._before)
            self._stop_edit()
            self.clearFocus()
            return
        super().keyPressEvent(event)

    def _start_edit(self):
        self._before = self.text()
        self.setReadOnly(False)
        self.setFrame(True)
        self.setStyleSheet("")
        self.setCursor(QtCore.Qt.CursorShape.IBeamCursor)
        self.selectAll()
        self.setFocus(QtCore.Qt.FocusReason.MouseFocusReason)

    def _stop_edit(self):
        self.setReadOnly(True)
        self.setFrame(False)
        self.setStyleSheet("background: transparent;")
        self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        self.deselect()

    def _commit(self):
        if self.isReadOnly():  # focus-out after Escape / after a commit
            return
        self._stop_edit()

        text = self.text().strip()
        if not text:  # refuse to blank a task
            self.setText(self._before)
            return
        self.setText(text)
        if text != self._before:
            self._on_commit(text)

