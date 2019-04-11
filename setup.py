from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='nail.ssgbase',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['nail-ssg = nail_ssg_base.commands:run']
    },
    install_requires=[
        'click==6.7',
        'ruamel.yaml==0.13.14',
        'nail-config>=0.1',
    ],
    dependency_links=[
        'https://github.com/nail-ssg/nail-config/archive/release/v0.1.zip#egg=nail-config-0.1'
    ]
)
