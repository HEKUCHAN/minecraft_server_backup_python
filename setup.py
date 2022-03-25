# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup, find_packages

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text()

setup(
    name='minecraft_backup',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>=3.5',
    entry_points={
        'console_scripts': {
            'minecraft-backup=minecraft_backup.main:main'
        }
    },
    description="""\
        This is a backup management library for Minecraft servers.
        It should be run and used on a regular basis using cron or similar.
    """,
    author='Heitor Hirose',
    author_email='Heitorhirose@gmail.com',
    url='https://github.com/HEKUCHAN/minecraft_server_buckup_python'
)
