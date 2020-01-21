#!/usr/bin/env python3
import pluribus.error as error

def open_file(path, mode):
	try:
		return open(path, mode)
	except (FileNotFoundError, IsADirectoryError):
		error.open_file(path)
