import dataclasses
from enum import Enum

SETTING_CLASSES = {}


def settings_register(cls):
    SETTING_CLASSES[cls.__name__] = cls
    return cls



DEFAULT_SETTINGS = {

}

def default_setting(name:str):
    def wrap(cls):
        DEFAULT_SETTINGS[name.lower().strip()] = cls.default(cls)
        return cls
    return wrap

@dataclasses.dataclass
class Preset:

    time_sec:int
    pause_time_sec:int

    preset_id:int = 0

class Status(Enum):

    unfinished = "unfinished"
    finished = "finished"

@dataclasses.dataclass
class Task:

    text:str
    status:Status = Status.unfinished

    def set_finished(self):
        self.status = Status.finished