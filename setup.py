# encoding=utf8
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name="django-ordermodel",
    version="0.0.1",
    url='http://github.com/MagicSolutions/django-ordermodel',
    description="Intends to help you create models which can bemoved up\down (or left\right) with respect to each other.",
    long_description=README,

    author='Kirill Elagin',
    author_email='kirelagin@gmail.com',
    packages=[
        'ordermodel',
    ],
    package_data={
        'ordermodel': [
            'static/ordermodel/*.gif',
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
