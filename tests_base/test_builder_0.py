import os

import pytest
# Создать объект builder
from nail_ssg_base.builder import Builder


def full_path(filename):
    return os.path.join(os.path.dirname(__file__), 'data', filename)


@pytest.fixture()
def empty_builder():
    filename = full_path('config_minimal.yml')
    print(filename)
    return Builder(filename)


def test_builder(empty_builder):
    # empty_builder.add_module('pages')
    empty_builder.build()
