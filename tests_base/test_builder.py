import pytest
from nail_ssg_base.builder import Builder


@pytest.fixture()
def empty_data():
    return '---'


@pytest.fixture()
def main_module_data():
    return '00. core: {"main": "nail_ssg_standard.modules.main"}'


@pytest.fixture()
def plugin_data():
    return ('---'
            '00. core:'
            '  src: src1'
            '  dist: site'
            '  currentNamespace: default'
            '  modules:'
            '    nail_ssg_standard.modules.pages: true'
            '    nail_ssg_standard.modules.static: true'
            '  main: nail_ssg_standard.modules.main'
            '10. scan:'
            '  order:'
            '  - nail_ssg_standard.modules.pages'
            '  - nail_ssg_standard.modules.static')


# [+] Подключение встроенных модулей к генератору
def test_plugin(plugin_data):
    builder = Builder(data=main_module_data)

    assert len(builder.config.modules) == 8


#  [+] Загрузка модуля main
def test_main_module(main_module_data):
    from nail_ssg_standard.modules.main import SsgMain

    builder = Builder(data=main_module_data)

    assert isinstance(builder.config.main_module, SsgMain)


#  [-] Подключение внешних модулей к генератору
def test_file_rule(main_module_data):
    builder = Builder(data=main_module_data)
    assert builder

#  [+] Загрузка файла конфигурации
#  [+] Подключение обработчика регистрации файла
#  [+] Вынести "список модулей" в отдельный модуль
