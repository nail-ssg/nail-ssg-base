from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='nail-ssg-base',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['nail-ssg = nail_ssg_base.commands:run']
    },
    install_requires=[
        'git+https://github.com/nail-ssg/nail-config@v0.1',
        'click==6.7',
        'ruamel.yaml==0.13.14'
    ])
