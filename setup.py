from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
	name='Texy.py',
	version='1.0.0',
	description='A library for text-based games',
	author='Thirsty-Robot',
	author_email='Thirsty-Robot@protonmail.com',
	license='MIT',

	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Games/Entertainment',
		'Topic :: Software Development :: Libraries  '
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3'
	],

	keywords='games game-engine text',
	packages=["Texy"]

	)