import importlib
from collections import OrderedDict

from nail_config.config import Config


class ConfigEx(Config):
    """docstring for ConfigEx"""

    def __init__(self):
        super().__init__()
        self.modules = OrderedDict()
        self.data = {}
        self.full_src_path = ''
        self.full_dst_path = ''
        self._main_module = None

    def add_module(self, module_name):
        if module_name not in self.modules:
            try:
                m = module_name.rsplit('.', 1)
                if len(m) == 1:
                    module = importlib.import_module(m[0])
                else:
                    module = getattr(importlib.import_module(m[0]), m[1])
            except Exception as e:
                raise e
            self.modules[module_name] = module.create(self)
            modules = self('00. core/modules')
            if modules:
                for name in modules:
                    if modules[name]:
                        self.add_module(name)
        return self._get_module(module_name)

    def _get_module(self, module_name):
        return self.modules.get(module_name, None)

    def get_module(self, module_name):
        module = self._get_module(module_name)
        # Есть опасность, что add_module приведёт к проблемам, для модулей упомянутых в config.*.order
        return self.add_module(module_name) if module is None else module

    def set_data(self, path, value):
        self.data[path] = value

    def get_data(self, path):
        return self.data.get(path, None)

    @property
    def main_module(self):
        if self.changed or not self._main_module:
            main_module_name = self('00. core/main')
            self._main_module = self.add_module(main_module_name)
        return self._main_module
