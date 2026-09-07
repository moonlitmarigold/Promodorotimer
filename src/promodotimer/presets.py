import dataclasses
from .vars import default_setting, Preset

@default_setting('presets')
@dataclasses.dataclass
class Presets: # Preset

    _list:list[Preset]
    _cur_presets_id = 0

    @classmethod
    def load(cls, *args):
        _l = list()
        for arg in args:
            _l.append(Preset(**arg))
        return cls(_l)

    def add(self, _p:Preset):
        _p.preset_id = len(self._list)
        self._list.append(_p)

    def remove(self, _id):
        del self._list[_id]

    @property
    def all(self):
        return self._list

    @property
    def cur_preset(self):
        return self._list[self._cur_presets_id]

    def set_preset(self, _id):
        self._cur_presets_id = _id

    @staticmethod
    def default(cls):
        return cls.load(*[dataclasses.asdict(Preset(25 * 60, 5 * 60))])
