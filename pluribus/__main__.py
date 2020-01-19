#!/usr/bin/env python3
import sys
from pluribus.input import get_config_file_path

def main(args=None):
	if args is None:
		args = sys.argv
	
	config_file_path = get_config_file_path(args)

if __name__ == "__main__":
	main()
