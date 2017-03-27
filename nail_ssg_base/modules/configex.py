import importlib
from nail_config.config import Config
from collections import OrderedDict


class ConfigEx(Config):

    """docstring for ConfigEx"""

    def __init__(self):
        super().__init__()
        self.modules = OrderedDict()
        self.data = {}
        self.full_src_path = ''
        self.full_dst_path = ''

    def add_module(self, module_name):
        if module_name not in self.modules:
            try:
                m = module_name.rsplit('.')
                if len(m) == 1:
                    module = importlib.import_module(m[0])
                else:
                    module = importlib.import_module(m[1], package=m[0])
            except Exception as e:
                raise e
            self.modules[module_name] = module.create(self)
            modules = self('core/modules')
            if modules:
                for name in modules:
                    if modules[name]:
                        self.add_module(name)
        return self._get_module(module_name)

    def _get_module(self, module_name):
        return self.modules[module_name] if module_name in self.modules else None

    def get_module(self, module_name):
        module = self._get_module(module_name)
        return self.add_module(module_name) if module is None else module
