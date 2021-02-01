#!/usr/bin/env python3
import os
import pluribus.error as error
from pluribus.config import Config

class PluribusDir:
	def __init__(self, config):
		self.path = get_directory(config.makefile) + "/" + config.pluribus_directory
		
		if not directoy_exists(self.path):
			create_directory(self.path)
