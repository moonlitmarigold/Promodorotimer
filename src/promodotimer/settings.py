from pathlib import Path
from PySide6 import QtCore
from dataclasses import dataclass
from . import presets as _presets
import json
from .vars import SETTING_CLASSES, DEFAULT_SETTINGS
from pydantic import BaseModel, ValidationError
from pydantic.fields import Field


class Settings(BaseModel):

    presets:_presets.Presets = Field(default_factory=lambda: DEFAULT_SETTINGS.get('presets'))

    @staticmethod
    def config_path() -> Path:
        # Linux:   ~/.config/promodotimer/settings.json
        # Windows: C:/Users/<you>/AppData/Local/promodotimer/settings.json
        base = QtCore.QStandardPaths.writableLocation(
            QtCore.QStandardPaths.StandardLocation.AppConfigLocation
        )
        return Path(base) / "promodo_settings.json"

    @classmethod
    def load(cls, override:Path | None = None):
        path = Settings.config_path() if not override else override

        if not path.exists():
            return cls()
        try:
            return cls.model_validate_json(path.read_text(encoding="utf-8"))
        except (ValidationError, OSError, ValueError):
              return cls()

    def save(self, override:Path | None = None) -> None:
        path = Settings.config_path() if not override else override
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(self.model_dump_json(indent=2), encoding="utf-8")
        tmp.replace(path)








