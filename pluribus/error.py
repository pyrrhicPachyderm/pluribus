#!/usr/bin/env python3
import sys

def err(err_string):
	print(err_string, file=sys.stderr)
	exit(1)

def usage(args):
	err("Usage: pluribus <config file>")

def change_directory(dir_path):
	err("Cannot move to directory {}".format(dir_path))

def create_directory(dir_path):
	err("Cannot create directory {}".format(dir_path))

def open_file(file_path):
	err("Cannot open file: {}".format(file_path))

def safety_line(file_path):
	err("Will not overwrite {}; file not created by Pluribus\nUse disable_safety = true to override".format(file_path))

def toml_parse(err_string):
	err("Error parsing config file: {}".format(err_string))

def type(variable_name, required_type):
	err("'{}' must be of type {}".format(variable_name, required_type.__name__))

def option_not_set(option_name):
	err("'{}' must be set".format(option_name))

def invalid_option(option_name):
	err("'{}' is not a valid option".format(option_name))
