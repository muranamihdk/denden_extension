# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup (
    name='denden_extension',
    version='1.0.1',
    author="Hideaki Muranami",
    description='Python-Markdown extension for DenDenMarkdown',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/muranamihdk/denden_extension',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: Markdown',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='Python-Markdown DenDenMarkdown DTP epub typesetting Japanese ruby でんでんマークダウン 電子書籍 組版 日本語 ルビ',
    py_modules=['denden_extension'],
    install_requires=['markdown>=2.6'],
)

