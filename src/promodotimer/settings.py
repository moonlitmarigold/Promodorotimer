from pathlib import Path
from PySide6 import QtCore
from dataclasses import dataclass
from . import presets
import json
from .vars import SETTING_CLASSES, DEFAULT_SETTINGS
from pydantic import BaseModel, ValidationError


class Settings(BaseModel):

    presets:list[presets.Preset] = DEFAULT_SETTINGS.get('presets')

    @staticmethod
    def config_path() -> Path:
        # Linux:   ~/.config/promodotimer/settings.json
        # Windows: C:/Users/<you>/AppData/Local/promodotimer/settings.json
        base = QtCore.QStandardPaths.writableLocation(
            QtCore.QStandardPaths.StandardLocation.AppConfigLocation
        )
        return Path(base) / "promodo_settings.json"

    @classmethod
    def load(cls):
        path = Settings.config_path()

        if not path.exists():
            return cls()
        try:
            return cls.model_validate_json(path.read_text(encoding="utf-8"))
        except (ValidationError, OSError, ValueError):
              return cls()

    def save(self) -> None:
        path = self.config_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(self.model_dump_json(indent=2), encoding="utf-8")
        tmp.replace(path)








