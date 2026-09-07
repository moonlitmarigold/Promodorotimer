from promodotimer import settings
from promodotimer.settings import Settings
from pathlib import Path
import json

test_settings = Path(__file__).parent / 'test_settings.json'
test_settings_output = Path(__file__).parent / 'test_settings_output.json'


def test_default_settings():

    s = Settings.load()

    print(s.presets)
    print(settings.DEFAULT_SETTINGS)

def test_save_settings():
    s = Settings.load()

    s.presets.add(settings._presets.Preset(70 * 60, 5 * 60))
    s.presets.add(settings._presets.Preset(10 * 60, 5 * 60))
    s.presets.add(settings._presets.Preset(20 * 60, 5 * 60))

    print(s.presets.all)
    print(s.presets)

    s.save(override=test_settings_output)

def test_load_settings():
    s = Settings.load(override=test_settings)

    print(s.presets)