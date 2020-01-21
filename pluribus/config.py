#!/usr/bin/env python3

from pluribus.options import set_options

class Config:
	_options_default = {
		"documentclass":"book",
		"documentclass_options":"",
		"disable_safety":false,
	}
	
	_options_type = {
		"documentclass":str,
		"documentclass_options":str,
		"disable_safety":bool,
	}
	
	def __init__(self, config_dict):
		options_dict = dict()
		for key, value in config_dict.items():
			if not isinstance(value, dict):
				options_dict[key] = value
		set_options(self, self._options_type, [options_dict, self._options_default])
