#!/usr/bin/env python3
from pluribus.config import Config
from pluribus.output import open_file_safe

class Makefile:
	_safety_line = "#Created by Pluribus."
	
	def print(self, line):
		print(line, file=self.file)
	
	def __init__(self, config):
		self.path = config.makefile
		self.standalone = config.makefile_standalone
		
		self.file = open_file_safe(self.path, "w", self._safety_line, config)
		self.print(self._safety_line)
