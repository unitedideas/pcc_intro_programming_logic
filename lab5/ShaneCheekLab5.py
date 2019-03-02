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


# from time import sleep
#
# from turtle import *
#
# name = ''
# first_last_name_list = []
# name_chr_list = []
#
#
# def letter_not_in_ascii():
#     """Input validation"""
#     first_name = ''
#     last_name = ''
#     while True:
#         first_name = input('First Name: ')
#         last_name = input('Last Name: ')
#         name = first_name + " " + last_name
#         if first_name and last_name != '':
#             return name
#
#
# def name_to_list(first_last_name_list):
#     """Set the full name list"""
#     for name in first_last_name_list:
#         name_chr_list.append(list(name))
#     return name_chr_list
#
#
# def name_total(name_chr_list):
#     """Total of all ascii characters in name"""
#     ascii_name_total = 0
#     for name in name_chr_list:
#         for character in name:
#             ascii_name_total += ord(character)
#     return ascii_name_total
#
#
# def display_name_ascii(name_chr_list):
#     """Print each character and ascii value"""
#     ascii_name_total = name_total(name_chr_list)
#     for name in name_chr_list:
#         for character in name:
#             print(character, ":", ord(character))
#     print(ascii_name_total, ":", chr(ascii_name_total))
#
#
# def turtle_time(name_chr_list, an_total):
#     pen = Turtle()
#     pen.screen.bgcolor('orange')
#     pen.screen.screensize(700, 700)
#     pen.hideturtle()
#     pen.speed(0)
#     pen.color('blue')
#     start_marker_y = 100
#     window_width = 350
#     for name in name_chr_list:
#         start_marker_x = (window_width / len(name)) - window_width
#         pen.penup()
#         pen.goto(start_marker_x, start_marker_y)
#         pen.pendown()
#         for character in name:
#             pen.penup()
#             pen.goto(start_marker_x, start_marker_y)
#             pen.pendown()
#             for count in range(ord(character)):
#                 pen.forward(count)
#                 pen.left(ord(character))
#             start_marker_x += (690 / len(name))
#         start_marker_y += -200
#     sleep(1.5)
#     pen.screen.clear()
#
#     pen.goto(0, 0)
#
#     for count in range(int(an_total / 3.5)):
#         pen.screen.bgcolor('orange')
#         pen.color('blue')
#         pen.forward(count)
#         pen.left(an_total)
#     sleep(2.5)
#
#
# name = letter_not_in_ascii()
#
# first_last_name_list = list(name.split(' '))
#
# name_chr_list = name_to_list(first_last_name_list)
#
# display_name_ascii(name_chr_list)
#
# turtle_time(name_chr_list, name_total(name_chr_list))

# remove below
import string
from random import randrange, randint
# remove above


from time import sleep

from turtle import *

name = ''
first_last_name_list = []
name_chr_list = []


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


def name_to_list(first_last_name_list):
    """Set the full name list"""
    for name in first_last_name_list:
        name_chr_list.append(list(name))
    return name_chr_list


def name_total(name_chr_list):
    """Total of all ascii characters in name"""
    ascii_name_total = 0
    for name in name_chr_list:
        for character in name:
            ascii_name_total += ord(character)
    return ascii_name_total


def display_name_ascii(name_chr_list):
    """Print each character and ascii value"""
    ascii_name_total = name_total(name_chr_list)
    for name in name_chr_list:
        for character in name:
            print(character, ":", ord(character))
    print(ascii_name_total, ":", chr(ascii_name_total))


def turtle_time(name_chr_list, an_total):
    window_width = 350
    pen = Turtle()
    pen.screen.screensize(window_width, window_width, 'orange')
    pen.hideturtle()
    pen.speed(0)
    pen.color('blue')
    start_marker_y = 100
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
            start_marker_x += (690 / len(name))
        start_marker_y += -200
    sleep(1.5)
    pen.screen.clear()

    pen.goto(0, 0)

    for count in range(int(an_total / 3.5)):
        pen.screen.screensize(canvwidth=700, canvheight=700, bg='orange')
        pen.color('blue')
        pen.forward(count)
        pen.left(an_total)
    sleep(2.5)
    # remove below
    pen.screen.clear()
    # remove above


rng = randint(0, len(string.printable)) - 1

name = string.printable[rng:rng + 5] + " " + string.printable[rng:rng + 5]

first_last_name_list = list(name.split(' '))

name_chr_list = name_to_list(first_last_name_list)

display_name_ascii(name_chr_list)

while True:
    turtle_time(name_chr_list, name_total(name_chr_list))
