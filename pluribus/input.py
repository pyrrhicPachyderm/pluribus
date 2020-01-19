#!/usr/bin/env python3
import sys
import toml

def print_usage_error(args):
	print("Usage: {} <config file>".format(args[0]), file=sys.stderr)
	exit(1)

def get_config_file_path(args):
	if(len(args) != 2):
		print_usage_error(args)
	else:
		return args[1]
