#!/usr/bin/env python3
from pluribus.options import set_options

class Config:
	_options_default = {
		"disable_safety":False,
		"makefile":"Makefile",
		"makefile_standalone":True,
		"pluribus_directory":".pluribus",
	}
	
	_options_type = {
		"disable_safety":bool,
		"makefile":str,
		"makefile_standalone":bool,
		"pluribus_directory":str,
	}
	
	def __init__(self, config_dict):
		options_dict = dict()
		#TOML tables, here representing volumes, are given as nested dictionaries.
		#First parse all keys that are general options, not volumes.
		#Volumes are handled in `volumes.py`.
		for key, value in config_dict.items():
			if not isinstance(value, dict):
				options_dict[key] = value
		set_options(self, self._options_type, [options_dict, self._options_default])
