#!/usr/bin/env python3
import sys

def err(err_string):
	print(err_string, file=sys.stderr)
	exit(1)

def usage(args):
	err("Usage: pluribus <config file>")

def read(file_path):
	err("Cannot read file: {}".format(file_path))

def toml_parse(err_string):
	err("Error parsing config file: {}".format(err_string))

def type(variable_name, required_type):
	err("'{}' must be of type {}".format(variable_name, required_type.__name__))

def option_not_set(option_name):
	err("'{}' must be set".format(option_name))

def invalid_option(option_name):
	err("'{}' is not a valid option".format(option_name))
