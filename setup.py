from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='nail-ssg-base',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['nail-ssg = nail-ssg-base.commands:run']
    },
    install_requires=[
        'click==6.7',
        'ruamel.yaml==0.13.14'
    ])
