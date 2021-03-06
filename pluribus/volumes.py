#!/usr/bin/env python3
from pluribus.options import set_options

class Volume:
	_options_default = {
		"title":None,
		"content":None,
		"documentclass":"book",
		"documentclass_options":"",
	}
	
	_options_type = {
		"title":str,
		"content":str,
		"documentclass":str,
		"documentclass_options":str,
	}
	
	def __init__(self, tag, volume_dict, all_dict):
		self.tag = tag
		set_options(self, self._options_type, [volume_dict, all_dict, self._options_default])

class VolumeContainer:
	_reserved_tags = ["all", "omnibus", "pluribus"]
	
	volumes = dict()
	
	def __init__(self, config_dict):
		#First, get the options that should be applied to all volumes.
		all_dict = config_dict.get("all", dict())
		#Next, get the individual (non-reserved) volumes.
		#Volumes are represented by nested dictionaries within the config dictionary.
		for key, value in config_dict.items():
			if isinstance(value, dict) and not key in self._reserved_tags:
				self.volumes[key] = Volume(key, value, all_dict)
