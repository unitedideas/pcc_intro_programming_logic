import time
import random

from turtle import *


name = input('First Name: ')
name += " "
name += input('Last Name: ')

name_to_char_list = list(name.split(' '))

names_in_2d_list = []

for name in name_to_char_list:
    names_in_2d_list.append(list(name))

print(names_in_2d_list)

totName = 0

for name in names_in_2d_list:
    for character in name:
        totName += ord(character)
        print(ord(character))
print(totName)
print(chr(totName))

joe = Turtle()
joe.hideturtle()
joe.speed(1000)
joe.color('red', 'yellow')
start_marker_y = 100
window_width = 350
for name in names_in_2d_list:
    start_marker_x = (window_width / len(name)) - window_width
    joe.penup()
    joe.goto(start_marker_x, start_marker_y)
    joe.pendown()
    for character in name:
        joe.penup()
        joe.goto(start_marker_x, start_marker_y)
        joe.pendown()
        for count in range(ord(character)):
            joe.forward(count)
            joe.left(ord(character))
        start_marker_x += (690 / len(name))
    start_marker_y += -200
time.sleep(13.5)