#!/usr/bin/env python3
import os
import pluribus.error as error

def get_directory(file_path):
	"""Gets the directory in which the file resides."""
	return os.path.dirname(file_path)

def change_directory(path):
	try:
		os.chdir(path)
	except (FileNotFoundError, NotADirectoryError):
		error.change_directory(path)

def file_exists(file_path):
	return os.path.isfile(file_path)

def directory_exists(directory_path):
	return os.path.isdir(directory_path)

def create_directory(directory_path):
	try:
		os.mkdir(directory_path)
	except:
		error.create_directory(directory_path)
