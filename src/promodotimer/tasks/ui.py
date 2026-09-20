from vars import Task
from .logic import Tasks, Task, Status
from ..settings import Settings
from PySide6 import QtCore, QtWidgets, QtGui
from ..ui import EditableLabel

class TaskRow(QtWidgets.QWidget):

    def __init__(self, task: Task, on_finish, on_delete, on_rename, parent=None):
        super().__init__(parent)

        self.task = task

        self.label = EditableLabel(
            task.text, lambda text, t=task: on_rename(text, t)
        )
        if task.status is Status.finished:
            font = self.label.font()
            font.setStrikeOut(True)
            self.label.setFont(font)

        self.finish_button = QtWidgets.QPushButton("✓")
        self.finish_button.setFixedWidth(30)
        self.finish_button.setEnabled(task.status is not Status.finished)
        self.finish_button.clicked.connect(lambda *_, t=task: on_finish(t))

        self.delete_button = QtWidgets.QPushButton("✕")
        self.delete_button.setFixedWidth(30)
        self.delete_button.clicked.connect(lambda *_, t=task: on_delete(t))

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.finish_button)
        layout.addWidget(self.delete_button)

class TasksUI:

    def __init__(self, main_window, settings:Settings):

        self.settings = settings
        self.main_window = main_window

        self.logic = Tasks()

        self.tasks_label = QtWidgets.QLabel("Tasks")

        self.task_button = QtWidgets.QPushButton("Add Task")
        self.task_button.clicked.connect(self.on_add_task)

        self.task_list_layout = QtWidgets.QVBoxLayout()

    def add_to_layout(self, layout:QtWidgets.QVBoxLayout):
        layout.addStretch()
        layout.addWidget(self.tasks_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(self.task_list_layout)
        layout.addWidget(self.task_button, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()
        self.refresh()

    def refresh(self):
        while (item := self.task_list_layout.takeAt(0)) is not None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for task in self.logic.all:
            self.task_list_layout.addWidget(
                TaskRow(task, self.on_finish_task ,self.on_delete_task, self.on_rename)
            )

    @QtCore.Slot()
    def on_delete_task(self, task):
        self.logic.delete(task)
        self.refresh()

    @QtCore.Slot()
    def on_finish_task(self, task):
        task.set_finished()
        self.refresh()

    @QtCore.Slot()
    def on_rename(self, text, task):
        self.logic.rename(task, text)
        self.refresh()

    @QtCore.Slot()
    def on_add_task(self):
        self.logic.add(Task(
            f"Task{len(self.logic.all)+1}"
            )
        )
        self.refresh()