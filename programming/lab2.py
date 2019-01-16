__author__ = "Shane Cheek"

# inputs:
# Formula for converting Fahrenheit to Celsius  (f − 32) × 5/9 = converted
# Formula for converting Fahrenheit to Kelvin   (f - 32) * 5/9 + 273.15 = converted
# Formula for converting Celsius to Fahrenheit  (c * 9/5) + 32 = converted
# Formula for converting Celsius to Kelvin      c + 273.15 = converted
# Formula for converting Kelvin to Celsius      k - 273.15 = converted
# Formula for converting Kelvin to Fahrenheit   (K - 273.15) * 9/5 + 32 = converted
# unit_options c,f,k

# process:
# calculation

# output:
# calculation


# pseudocode:
# if do_again is true
# create options
"""display instructions options "C, K or F" for Celsius, Kelvin or Fahrenheit
and ask for input conversion from "C, K or F"""
# get from quantity
# check if C,F or K were inputs
# remove selection from options
# ask for input conversion to "C, K or F", but not the same as previously selected
# check if input is an option remaining in unit_options
# calculate conversion
# display input1 + " = " calculation_output + input2
# ask if they want to do it again
# bye bye

do_again = "y"

while do_again == "y":
    unit_options = ["c", 'f', 'k']

    unit_from = input(
        'We will convert between Fahrenheit, Celsius or Kelvin. \n'
        'Please select the unit you want to convert from. \n'
        'Type f for Fahrenheit, c for Celsius or k for Kelvin:\n').lower()

    if unit_from not in unit_options:
        while unit_from not in unit_options:
            unit_from = input(
                str(unit_from) + ' is not an option please choose ' + unit_options[0] + ' or ' + unit_options[
                    1] + ' or ' +
                unit_options[2] + '\n').lower()

    unit_options.remove(unit_from)

    while True:
        try:
            qty_from = float(input('Enter a quantity. \n'))
            break
        except ValueError:
            print("That is not a number.")

    unit_to = input(
        'Please select the unit you want to convert to, but not the same as converting from.  \n'
        'Please choose ' + unit_options[0] + ' or ' + unit_options[1] + '\n').lower()

    if unit_to not in unit_options:
        while unit_to not in unit_options:
            unit_to = input(
                str(unit_to) + ' is not an option please choose ' + unit_options[0] + ' or ' + unit_options[
                    1] + '\n').lower()

    formulas = {
        "c": {"f": qty_from * (9 / 5) + 32, "k": qty_from + 273.15},
        "f": {"c": (qty_from - 32) * (5 / 9), "k": (qty_from - 32) * 5 / 9 + 273.15},
        'k': {"c": qty_from - 273.15, "f": qty_from + 273.15}}

    conversion = formulas[unit_from][unit_to]
    print(conversion)
    print(str(qty_from) + " " + str(unit_from) + " = " + str(conversion) + " " + str(unit_to))

    do_again = input('Do another? y = yes, n = no\n').lower()

    if do_again != "y" and do_again != "n":
        while do_again != "y" and do_again != "n":
            do_again = input('Do another? y = yes, n = no\n').lower()
print("Bye Bye")
