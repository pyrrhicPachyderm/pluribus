#!/usr/bin/env python3
import sys
import toml
import pluribus.error as error

def get_config_file_path(args):
	if len(args) != 1:
		error.usage(args)
	else:
		return args[0]

def read_config_file(config_file_path):
	try:
		return toml.load(config_file_path)
	except (FileNotFoundError, IsADirectoryError):
		error.open_file(config_file_path)
	except toml.decoder.TomlDecodeError as err_string:
		error.toml_parse(err_string)
