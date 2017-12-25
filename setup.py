"""
expylain is a Python package for Jupyter notebooks that enables rapid
interactive exploration of random processes. It is designed for ease-of-use in
learning contexts.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='expylain',
    version='0.0.1',
    description="""
    expylain is a Python package for Jupyter notebooks that enables rapid
    interactive exploration of random processes. It is designed for ease-of-use
    in learning contexts.
    """,
    long_description=long_description,
    url='https://github.com/SamLau95/expylain',

    author='Sam Lau',
    author_email='samlau95@gmail.com',

    license='BSD 3-Clause',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Jupyter',
    ],
    keywords='jupyter expylain visualization random',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
    ],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
