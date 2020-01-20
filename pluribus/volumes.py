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
