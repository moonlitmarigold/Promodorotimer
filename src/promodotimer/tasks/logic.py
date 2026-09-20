from .vars import Task, Status
import dataclasses

@dataclasses.dataclass
class Tasks:

    _tasks:list[Task] = dataclasses.field(default_factory=[])
    cur_id = 0

    def add(self, t:Task):
        self._tasks.append(t)

    @property
    def all(self):
        return self._tasks

    def delete(self, _id):
        del self._tasks[_id]

        if _id == self.cur_id:
            if self.cur_id == len(self._tasks):
                self.cur_id -= 1

    @property
    def display_current(self):
        if self.cur_id == len(self._tasks):
            return None
        return self._tasks[self.cur_id]

    def finish_current(self):
        self._tasks[self.cur_id].status = Status.finished
        self.cur_id += 1
