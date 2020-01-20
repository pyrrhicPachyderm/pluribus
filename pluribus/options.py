#!/usr/bin/env python3
import pluribus.error as error

#If an option has a type, but no default (or a None default), it is mandatory.

def set_option(obj, option, option_type, option_values):
	"""Set the value of an option from a list of possible values.
	
	Search option_values for the first non-None value.
	Set <obj>.<option> to this value.
	If all the values are None, return None.
	If any of the values doesn't match option_type (and isn't None), error.
	"""
	
	#Check all the types first.
	for option_value in option_values:
		if option_value != None and not isinstance(option_value, option_type):
			error.type(option, option_type)
	
	#Then select a value.
	for option_value in option_values:
		if option_value != None:
			setattr(obj, option, option_value)
			return
	
	#No valid value found.
	error.option_not_set(option)

def set_options(obj, type_dict, option_dicts):
	"""Set all the options defined by type_dict, given a list of dictionaries with possible values.
	
	option_dicts are searched in order, with earlier entries having higher priority.
	Every option in type_dict must be given a non-None value in one of the option_dicts.
	Conversely, every value in every one of the option_dicts must have a corresponding
	entry in type_dict.
	"""
	
	#First, check that all entries in all option_dicts are matched in type_dict.
	option_set = set()
	for option_dict in option_dicts:
		option_set |= option_dict.keys()
	for option in option_set:
		if not option in type_dict:
			error.invalid_option(option)
	
	#Next, set the values for entries in type_dict.
	for option, option_type in type_dict.items():
		option_values = []
		for option_dict in option_dicts:
			option_values.append(option_dict.get(option, None))
		set_option(obj, option, option_type, option_values)
