try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys



config = {
    'description': 'backend is a template python project for structuring a backend json api and database',
    'author': 'Jason Shiverick',
    'url': '...',
    'download_url': 'Where to download it.',
    'author_email': 'jshiv00@gmail.com',
    'version': '0.0.0',
    'install_requires': ['nose','pymongo','falcon'],
    'dependency_links': [
    ],
    'packages': ['backend'],
    'scripts': [],
    'name': 'backend'
}

#install relpy
setup(**config)