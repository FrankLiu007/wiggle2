from setuptools import setup

setup(
    name='wiggle2',
    version='0.2',
    packages=['wiggle2'],
    author="liu qimin",
    author_email="liuqimin2009@163.com",
    url="https://github.com/FrankLiu007/wiggle2",
    install_requires=[
        'matplotlib; python_version >= "3.5"'
    ],
description="Utility to plot seismic data, inspired by [wiggle](https://github.com/lijunzh/wiggle) function. I provide more options, such as orientation, normalization method, scale. "
)