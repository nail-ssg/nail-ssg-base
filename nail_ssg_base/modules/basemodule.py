from nail_config import Config


class BaseModule(object):
    _default_config = {}  # dict
    _config_comments = {}  # dict
    __version__ = None  # string
    name = ''

    def __init__(self, config: Config):
        self.config = config
        config.add_default_config(self._default_config, self._config_comments)

    def init(self):
        pass
