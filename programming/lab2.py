__author__ = "Shane Cheek"

# inputs:
# Formula for converting Fahrenheit to Celsius (f − 32) × 5 / 9 = c
# Formula for converting Celsius to Kelvin (Celsius + 273.15 = Kelvin)
# unit_options c,f,k

# process:
# calculation

# output:
# calculation

# pseudocode
# create options
"""display instructions options "C, K or F" for Celsius, Kelvin or Fahrenheit
and ask for input conversion from "C, K or F"""
# check if C,F or K were inputs
# remove selection from options
# ask for input conversion to "C, K or F", but not the same as previously selected
# check if the 2 inputs are the same, if so ask again
# display input1 + " = " calculation_output + input2

unit_options = ["c", 'f', 'k']

unit_from = input(
    'We will convert between Fahrenheit, Celsius or Kelvin. \n'
    'Please select the unit you want to convert from. \n'
    'Type f for Fahrenheit, c for Celsius or k for Kelvin:\n').lower()

if unit_from not in unit_options:
    while unit_from not in unit_options:
        unit_from = input(
            str(unit_from) + ' is not an option please select f for Fahrenheit, c for Celsius or k for Kelvin:\n').lower()

unit_options.remove(unit_from)

unit_to = input(
    'Please select the unit you want to convert to, but not the same as converting from.  \n'
    'Please choose ' + unit_options[0] + ' or ' + unit_options[1] + '\n').lower()

if unit_to not in unit_options:
    while unit_from not in unit_options:
        unit_from = input(
            str(unit_to) + ' is not an option please choose ' + unit_options[0] + ' or ' + unit_options[1] + '\n').lower()

print(unit_to)
