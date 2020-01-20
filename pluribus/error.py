#!/usr/bin/env python3
import sys

def _print(err_string):
	print(err_string, file=sys.stderr)
	exit(1)

def usage(args):
	_print("Usage: pluribus <config file>")

def read(file_path):
	_print("Cannot read file: {}".format(file_path))