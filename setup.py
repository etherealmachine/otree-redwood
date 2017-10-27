import os
import re
import sys
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def read_version():
    with open('otree_redwood/__init__.py', 'r') as f:
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]",
            f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='otree-redwood',
    version=read_version(),
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='oTree extension for inter-page communication.',
    long_description=README,
    url='https://github.com/Leeps-Lab/otree-redwood',
    author='James Pettit',
    author_email='james.l.pettit@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Sphinx',
        'sphinx-autobuild',
        'sphinx-rtd-theme',
        'chan>=0.3.1,<1',
        'channels==1.1.6',
        'daphne>=1.0.0,<2',
        'Django==1.8.8',
        'jsonfield>=2,<3',
        'mockredispy>=2.9.0,<3'
    ] + ['asgi_redis==1.4.2'] if 'win' not in sys.platform else []
)
