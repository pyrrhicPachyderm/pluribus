#!/usr/bin/env python3
import sys
import toml

def print_usage_error(args):
	print("Usage: pluribus <config file>", file=sys.stderr)
	exit(1)

def get_config_file_path(args):
	if(len(args) != 1):
		print_usage_error(args)
	else:
		return args[0]

def read_config_file(config_file_path):
	return toml.load(config_file_path)
