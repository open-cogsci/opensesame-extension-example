#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
No rights reserved. All files in this repository are released into the public
domain.
"""

from setuptools import setup

setup(
	# Some general metadata. By convention, a extension is named:
	# opensesame-extension-[extension name]
	name='opensesame-extension-example_extension',
	version='0.0.1',
	description='Example extension for OpenSesame',
	author='Your Name',
	author_email='yourname@domain.com',
	url='https://github.com/your/repository',
	# Classifiers used by PyPi if you upload the extension there
	classifiers=[
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Environment :: X11 Applications',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
	],
	# The important bit that specifies how the extension files should be installed,
	# so that they are found by OpenSesame. This is a bit different from normal
	# Python modules, because an OpenSesame extension is not a (normal) Python
	# module.
	data_files=[
		# First the target folder.
		('share/opensesame_extensions/example_extension',
		# Then a list of files that are copied into the target folder. Make sure
		# that these files are also included by MANIFEST.in!
		[
			'opensesame_extensions/example_extension/example_extension.py',
			'opensesame_extensions/example_extension/info.yaml',
			]
		)]
	)
