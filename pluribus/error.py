#!/usr/bin/env python3
import sys

def err(err_string):
	print(err_string, file=sys.stderr)
	exit(1)

def usage(args):
	err("Usage: pluribus <config file>")

def read(file_path):
	err("Cannot read file: {}".format(file_path))
