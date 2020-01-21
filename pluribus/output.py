#!/usr/bin/env python3
import pluribus.error as error
import Config from pluribus.config

def open_file(path, mode):
	try:
		return open(path, mode)
	except (FileNotFoundError, IsADirectoryError):
		error.open_file(path)

def check_safety_line(path, safety_line):
	"""Return true if the file starts with the safety line."""
	with open_file(path, "r") as file:
		return file.readline().rstrip('\n') == safety_line

def open_file_safe(path, mode, safety_line, config):
	if config.disable_safety or check_safety_line(path, safety_line):
		return open_file(path, mode)
	else:
		error.safety_line(path)
