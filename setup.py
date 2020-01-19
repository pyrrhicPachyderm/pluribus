#!/usr/bin/env python3
from setuptools import setup

setup(
	name = "pluribus",
	version = "0.1.0",
	packages=["pluribus"],
	entry_points = {
		"console_scripts": [
			"pluribus = pluribus.__main__:main"
		]
	},
	install_requires=[
		'toml',
	],
)
