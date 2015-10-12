
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PyLexia',
    'author': 'Adam Kariv',
    'url': 'URL to get it at.',
    'author_email': 'adam@everything.me',
    'version': '0.1',
    'install_requires': ['python-Levenshtein'],
    'packages': ['pylexia'],
    'scripts': [],
    'name': 'pylexia'
}

setup(**config)
