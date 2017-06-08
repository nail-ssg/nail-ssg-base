class BaseModule(object):
    _default_config = {}     # dict
    _config_comments = {}    # dict
    __version__ = None       # string
    name = ''
    def __init__(self, config):
        self.config = config
        cls = self.__class__
        config.add_default_config(cls._default_config, cls._config_comments)

    def init(self):
        pass
