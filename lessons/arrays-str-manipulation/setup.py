try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'arrays_str_manipulation',
    'author': 'Neil Seward',
    'author_email': 'neil.seawrd@outlook.com',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'manip'
}

setup(**config)
