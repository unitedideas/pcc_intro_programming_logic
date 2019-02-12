__author__ = "Shane Cheek"

# inputs: unit_from, qty_from, unit_to
# output: Display "str(qty_from) + " " + str(unit_from) + " = " + str(conversion) + " " + str(unit_to)"


# Declare List unit_options
# Declare String unit_from
# Declare Real qty_from
# Declare String unit_to
# Declare Dict formulas
# Declare Real conversion
#
# Set unit_options
#
# Display 'We will convert between Fahrenheit, Celsius or Kelvin. \n'
#     'Please select the unit you want to convert from. \n'
#     'Type f for Fahrenheit, c for Celsius or k for Kelvin:\n'
#
# Input unit_from
#
# Set unit_options to the remaining two units != unit_from
#
# Display Enter a quantity. \n
#
# Input qty_from
#
# Display 'Please select the unit you want to convert to, but not the same as converting from.  \n'
#     'Please choose ' + unit_options[0] + ' or ' + unit_options[1] + '\n'
#
# Input unit_to
#
# Set conversion = formulas[unit_from][unit_to]
#
# Display str(qty_from) + " " + str(unit_from) + " = " + str(conversion) + " " + str(unit_to)




unit_options = []
unit_from = ''
qty_from = 0.0
unit_to = ''
formulas = {}
conversion = 0.0

unit_options = ["c", 'f', 'k']

unit_from = input(
    'We will convert between Fahrenheit, Celsius or Kelvin. \n'
    'Please select the unit you want to convert from. \n'
    'Type f for Fahrenheit, c for Celsius or k for Kelvin:\n').lower()

unit_options.remove(unit_from)

qty_from = float(input('Enter a quantity. \n'))

unit_to = input(
    'Please select the unit you want to convert to, but not the same as converting from.  \n'
    'Please choose ' + unit_options[0] + ' or ' + unit_options[1] + '\n').lower()

formulas = {
    "c": {"f": qty_from * (9 / 5) + 32, "k": qty_from + 273.15},
    "f": {"c": (qty_from - 32) * (5 / 9), "k": (qty_from - 32) * 5 / 9 + 273.15},
    'k': {"c": qty_from - 273.15, "f": qty_from + 273.15}}

conversion = formulas[unit_from][unit_to]

print(str(qty_from) + " " + str(unit_from) + " = " + str(conversion) + " " + str(unit_to))


