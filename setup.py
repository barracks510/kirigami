import os

from setuptools import setup, find_packages
from kirigami.version import VERSION

def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
        return f.read()

setup(
    name='kirigami',
    packages=find_packages(exclude=['docs', 'test']),
    version=VERSION,
    description='Taking PaperCut to the Next Level',
    long_description=readme(),
    license='AGPLv3+',
    url='https://src-code.simons-rock.edu/git/print-central/kirigami',
    author='Dennis Chen',
    author_email='barracks510@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'Topic :: Printing'
    ],
    install_requires=[
        'netifaces',
    ],
    entry_points={
        'console_scripts': [
            'kirigami=kirigami.cmd:cli'
        ],
    },
    zip_safe=False
)
