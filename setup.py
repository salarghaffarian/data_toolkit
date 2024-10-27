from setuptools import setup, find_packages

setup(
    name='data_toolkit', # Updated module name
    version='0.1',
    packages=find_packages(), 
    description='A toolkit for test the installability of a python package',
    author="Salar Ghaffarian",
    author_email="salarghaffarian1363@gmail.com",
    install_requires=[],
    python_requires='>=3.7'
)