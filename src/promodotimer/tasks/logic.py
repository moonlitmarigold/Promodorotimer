from vars import Task, Status
import dataclasses

@dataclasses.dataclass
class Tasks:

    _tasks:list[Task] = dataclasses.field(default_factory=lambda:[])
    cur_id = 0

    def add(self, t:Task):
        if self._tasks:
            t.internal_id = len(self._tasks)
        self._tasks.append(t)

    @property
    def all(self):
        return self._tasks

    def delete(self, task:Task):
        internal_id = task.internal_id
        index = None
        for i, t in enumerate(self.all):
            if t.internal_id == internal_id:
                index = i
                continue
        if index:
            del self._tasks[index]

    def rename(self, task, text):
        task.text = text

    @property
    def display_current(self):
        if self.cur_id == len(self._tasks):
            return None
        return self._tasks[self.cur_id]

    def finish_current(self):
        self._tasks[self.cur_id].status = Status.finished
        self.cur_id += 1
