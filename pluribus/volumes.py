#!/usr/bin/env python3
from pluribus.options import set_options

class Volume:
	_options_default = {
		"title":None,
		"content":None,
	}
	
	_options_type = {
		"title":str,
		"content":str,
	}
	
	def __init__(self, tag, volume_dict, all_dict):
		self.tag = tag
		set_options(self, self._options_type, [volume_dict, all_dict, self._options_default])

class VolumeContainer:
	_reserved_tags = ["all", "omnibus", "pluribus"]
	
	volumes = dict()
	
	def __init__(self, config_dict):
		all_dict = config_dict.get("all", dict())
		for key, value in config_dict.items():
			if isinstance(value, dict) and not key in self._reserved_tags:
				self.volumes[key] = Volume(key, value, all_dict)
