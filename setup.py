
from setuptools import setup
from setuptools import find_packages


version = '1.1.4'

long_description = 'Lamelgraph'

setup(
    name = 'Lamel_window',
    version = version,

    author = 'Nikita Goltsev',
    author_email = 'n.goltsev@g.nsu.ru',

    description = 'Lamelgraph project',
    long_description = long_description,

    url = 'https://github.com/NikitaGoltsev/Lamel_project_copy',

    packages = ['src/Lamel_window'],
    install_requires = ['numpy', 'pandas'],
    )