from nail_config import Config

from .basemodule import BaseModule


class BasePlugin(BaseModule):
    module_type = 'plugin'
    _default_config = None  # dict
    _config_comments = None  # dict
    __version__ = None  # string
    name = ''
    types = {}

    def __init__(self, config: Config):
        super().__init__(config)
        config.add_default_config(self._default_config, self._config_comments)

    def process_file(self, file_info, rules, data):
        pass

    def modify_data(self):
        pass

    def build(self):
        pass

    def get_data(self, path):
        return None
