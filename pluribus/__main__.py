#!/usr/bin/env python3
import sys
from pluribus.input import get_config_file_path

def main(args=None):
	if args is None:
		args = sys.argv[1:]
	
	config_file_path = get_config_file_path(args)
	config = read_config_file(config_file_path)

if __name__ == "__main__":
	main()
