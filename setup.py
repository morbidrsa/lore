#!/usr/bin/env python3

from setuptools import setup

setup(
    name="lore",
    version='0.0.1',
    author='Johannes Thumshirn',
    author_email='jth@kernel.org',
    description='Get message-ids for patches from lore.kernel.org',
    install_requires=[
        'beautifulsoup4==4.12.3',
        'soupsieve>=2.3',
        'argparse==1.4.0'

    ],
    entry_points={
        'console_scripts': ['lore=lore:main']
    },
)
