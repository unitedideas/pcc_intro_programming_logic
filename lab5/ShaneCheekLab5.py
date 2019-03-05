# Description:
#   This program will take 2 user inputs (first and last name) and
#   draw a pictogram for each letter in the first and last name.
#   Also, the output window will display the ascii character of
#   the combined total of all letters in the first and last name.
#   to do this we will use a 2D array

# Input
#   name: first name and last concatenated.

# Output:
#   1. Graphic interface that draws each letter
#   2. Letter and Ascii number for each character in the name
#   3. Ascii number and ascii character for the total ascii numbers in the combine name


# From time Import sleep
# From turtle Import All
from time import sleep

from turtle import *

# Declare String name = ''
# Declare Array first_last_name_list = []
# Declare Array name_chr_list = []
name = ''
first_last_name_list = []
name_chr_list = []


# Function String letter_not_in_ascii()
#     Declare String first_name = ''
#     Declare String last_name = ''
#     While True then
#         Set first_name = input('First Name: ')
#         Set last_name = input('Last Name: ')
#         Set name = first_name + " " + last_name
#         If first_name and last_name != '' then
#             Return name
#         Else:
#             Display 'You just enter a first and last name.'
#         End If
#      End While
# End Function
def letter_not_in_ascii():
    """Input validation"""
    first_name = ''
    last_name = ''
    while True:
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        name = first_name + " " + last_name
        if first_name and last_name != '':
            return name
        else:
            print('You just enter a first and last name.')


# Function Array name_to_list(Array first_last_name_list)
#     For name in first_last_name_list:
#         name_chr_list.append(list(name))
#     End For
#     Return name_chr_list
# End Function
def name_to_list(first_last_name_list):
    """Set the full name list"""
    for name in first_last_name_list:
        name_chr_list.append(list(name))
    return name_chr_list


# Function Int name_total(Array name_chr_list)
#     ascii_name_total = 0
#     For name in name_chr_list:
#         For character in name:
#             ascii_name_total += ord(character)
#     End For
#     End For
#     Return ascii_name_total
# End Function
def name_total(name_chr_list):
    """Total of all ascii characters in name"""
    ascii_name_total = 0
    for name in name_chr_list:
        for character in name:
            ascii_name_total += ord(character)
    return ascii_name_total


# Module display_name_ascii(Array name_chr_list)
#     ascii_name_total = name_total(name_chr_list)
#     For name in name_chr_list:
#         For character in name:
#             Display(character, ":", ord(character))
#     End For
#     Display(ascii_name_total, ":", chr(ascii_name_total))
# End Module
def display_name_ascii(name_chr_list):
    """Print each character and ascii value"""
    ascii_name_total = name_total(name_chr_list)
    for name in name_chr_list:
        for character in name:
            print(character, ":", ord(character))
    print(ascii_name_total, ":", chr(ascii_name_total))


# Module turtle_time(name_chr_list, an_total)
#     Declare Int window_width = 0
#     Decalre Int start_marker_y = 0
#     Set pen = Class Turtle()
#     Call pen.screen.bgcolor('orange')
#     Call pen.screen.screensize(700, 700)
#     Call pen.hideturtle()
#     Call pen.speed(0)
#     Call pen.color('blue')
#     Set start_marker_y = 100
#     Set window_width = 350
#     For name in name_chr_list
#         Declare Int start_marker_x = 0
#         Set start_marker_x = (window_width / len(name)) - window_width
#         Call pen.penup()
#         Call pen.goto(start_marker_x, start_marker_y)
#         Call pen.pendown()
#         For character in name
#             Call pen.penup()
#             Call pen.goto(start_marker_x, start_marker_y)
#             Call pen.pendown()
#             For count in range(ord(character))
#                 Set pen.Forward(count)
#                 Set pen.left(ord(character))
#                 Set start_marker_x += (window_width * 2 / len(name))
#         End For
#         Set start_marker_y += -200
#     End For
#     Call sleep(1.5)
#     Call pen.screen.clear()
#
#     Call pen.goto(0, 0)
#
#     For count in range(int(an_total / 3.5))
#         Set pen.screen.bgcolor('orange')
#         Set pen.color('blue')
#         Set pen.Forward(count)
#         Set pen.left(an_total)
#     End For
#     Call sleep(2.5)
# End Module
#
# Set name = letter_not_in_ascii()
#
# Call first_last_name_list = list(name.split(' '))
#
# Set name_chr_list = name_to_list(first_last_name_list)
#
# Call display_name_ascii(name_chr_list)
#
# Call turtle_time(name_chr_list, name_total(name_chr_list))
def turtle_time(name_chr_list, an_total):
    """Draws pictogram to the screen for each character in the list"""
    window_width = 0
    start_marker_y = 0
    pen = Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.screen.bgcolor('orange')
    pen.color('blue')
    start_marker_y = 100
    window_width = 350
    for name in name_chr_list:
        start_marker_x = (window_width / len(name)) - window_width
        pen.penup()
        pen.goto(start_marker_x, start_marker_y)
        pen.pendown()
        for character in name:
            pen.penup()
            pen.goto(start_marker_x, start_marker_y)
            pen.pendown()
            for count in range(ord(character)):
                pen.forward(count)
                pen.left(ord(character))
            start_marker_x += (window_width * 2 / len(name))
        start_marker_y += -200
    sleep(1.5)
    pen.screen.clear()
    pen.screen.bgcolor('orange')

    pen.goto(0, 0)

    for count in range(int(an_total / 3)):
        pen.color('blue')
        pen.forward(count)
        pen.left(an_total)
    sleep(2.5)


name = letter_not_in_ascii()

first_last_name_list = list(name.split(' '))

name_chr_list = name_to_list(first_last_name_list)

display_name_ascii(name_chr_list)

turtle_time(name_chr_list, name_total(name_chr_list))
