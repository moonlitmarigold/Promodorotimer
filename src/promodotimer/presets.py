import dataclasses
from .vars import default_setting

@default_setting('preset')
@dataclasses.dataclass
class Preset: # Preset

    preset_id:int
    time_sec:int


    def to_json(self):
        return {
            "preset_id":self.preset_id,
            "time_sec":self.time_sec
        }

    @classmethod
    def load(cls, **kwargs):
        return cls(**kwargs)

    @staticmethod
    def default():
        return [dataclasses.asdict(Preset(0, 25 * 60))]