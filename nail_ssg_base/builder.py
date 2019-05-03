import os
from shutil import rmtree

from .dir_runner import DirRunner
from .modules import ConfigEx


class Builder(object):
    _file_loaded = False
    config = None

    def _load_config(self, data=None, filename=''):
        self.config = ConfigEx()
        # if not self.config.load(filename):
        #     raise Exception('OMG')
        if not data and not filename:
            raise Exception('set value in filename or source parameter')
        if filename:
            self._file_loaded = self.config.load(filename)
        else:
            self.config.loads(data)
            self._file_loaded = True
        default_config = {
            '00. core':
                {
                    'src': 'src',
                    'dest': 'site',
                    'currentNamespace': 'default',
                    'main': 'nail_ssg_standard.main',
                },
            '10. scan': {
                'order': [],
                'types': {}
            },
            '30. modify': {
                'order': [],
                'options': []
            },
            '40. build': {
                'order': []
            }
        }
        config_comments = {
            '10. scan': 'Step #1',
            '30. modify': 'Step #2',
            '40. build': 'Step #3',
            '00. core/modules': 'List of modules and they states',
            '00. core/dest': 'Destination directory for builded site',
            '00. core/src': 'Source of templates, site files and raw page data',
            '00. core/currentNamespace': 'Current namespace of aliases',
            '10. scan/order': 'Module list',
        }
        self.config.add_default_config(
            default_config,
            config_comments
        )

    def _init_modules(self):
        self.config.main_module # инициализация модулей
        for module_name in self.config.modules:
            module = self.config.modules[module_name]
            module.init()
        self.config.do_autosave()

    def __init__(self, filename='', data=None):
        # if not os.path.exists(filename):
        #     self.set_default_config()
        self._load_config(filename=filename, data=data)
        self.src = self.config('00. core/src')
        self.dst = self.config('00. core/dest')
        self.config.full_src_path = os.path.abspath(self.src)
        self.config.full_dst_path = os.path.abspath(self.dst)
        self.config.data = {
            'data': {},
        }
        self._init_modules()
        self.scan_order = self.config('10. scan/order', [])
        # print(self._modules)
        # print(self.config.as_yamlstr())
        # print(self.config)

    def build(self):
        dr = DirRunner(self.src, self._file_handler)
        dr.run()
        # print('='*20)
        # yprint(self.config.data)
        # print('='*20)
        self.config.main_module.modify_data()
        for module_name in self.config('30. modify/order'):
            module = self.config.modules[module_name]
            module.modify_data()
        print(f'Removing folder "{self.config.full_dst_path}" before build')
        rmtree(self.config.full_dst_path, True)
        self.config.main_module.build()
        for module_name in self.config('40. build/order'):
            module = self.config.modules[module_name]
            module.build()

    def _file_handler(self, dr: DirRunner, full_path: str, is_dir: bool) -> bool:
        if is_dir:
            return True
        data = {}
        rules = {}
        folder, name = full_path.rsplit(os.sep, 1)
        file_info = {
            'directory': folder,
            'name': name,
            'full_path': full_path
        }
        rel_path = os.path.relpath(full_path, self.config.full_src_path).replace(os.sep, '/')
        self.config.main_module.process_file(file_info, rules, data)
        for module_name in self.scan_order:
            module = self.config.modules[module_name]
            module.process_file(file_info, rules, data)
        self.config.set_data(rel_path, data)
        return True

    def set_default_configs(self):
        for key in self.config.modules:
            module = self.config.modules[key]
            default_core_config, core_comments = module.get_default_config()
            self.set_default_config(default_core_config, core_comments)

    def set_default_config(self, dconf, comments=None):
        self.config.add_default_config(dconf, comments)
