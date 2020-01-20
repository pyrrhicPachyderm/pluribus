#!/usr/bin/env python3
import pluribus.error as error

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
