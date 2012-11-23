# encoding=utf8
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name="django-orderedmodel",
    version="0.1.2",
    url='http://github.com/MagicSolutions/django-orderedmodel',
    description="Intends to help you create models which can bemoved up\down (or left\right) with respect to each other.",
    long_description=README,

    author='Kirill Elagin',
    author_email='kirelagin@gmail.com',
    packages=[
        'orderedmodel',
    ],
    package_data={
        'orderedmodel': [
            'static/orderedmodel/*.gif',
            'static/orderedmodel/*.js',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django>=1.3',
    ],
)
