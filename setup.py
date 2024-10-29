from setuptools import setup, find_packages
setup (
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude= ['tests*']),
    licence = 'MIT',
    description = 'EDSA example package',
    long_description = open ('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/JoshuaWario12/mypackage',
    author = 'Joshua',
    email = 'galgewariyo@gmail.com'
)