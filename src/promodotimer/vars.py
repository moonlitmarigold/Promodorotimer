SETTING_CLASSES = {}


def settings_register(cls):
    SETTING_CLASSES[cls.__name__] = cls
    return cls



DEFAULT_SETTINGS = {

}

def default_setting(cls, name):
    DEFAULT_SETTINGS[name] = cls.default()
    return cls