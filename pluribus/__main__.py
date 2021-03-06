#!/usr/bin/env python3
import sys
from pluribus.input import get_config_file_path, read_config_file
from pluribus.files import get_directory, change_directory
from pluribus.volumes import VolumeContainer
from pluribus.config import Config
from pluribus.makefile import Makefile

def main(args=None):
	if args is None:
		args = sys.argv[1:]
	
	config_file_path = get_config_file_path(args)
	config_dict = read_config_file(config_file_path)
	
	change_directory(get_directory(config_file_path))
	
	config = Config(config_dict)
	volume_container = VolumeContainer(config_dict)
	makefile = Makefile(config)
	pluribus_dir = PluribusDir(config)

if __name__ == "__main__":
	main()
