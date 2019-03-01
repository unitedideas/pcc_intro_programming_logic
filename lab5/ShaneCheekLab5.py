import time
import random

from turtle import *

start = round(time.time()/(60*60*24*365)*2)

print(start)
name = input('first name')
name += ' '
name += input('last name')

stop = round(time.time()/(60*60*24*365)*2)
totalTime = round(stop - start)

sr = list(name.split(' '))

full_list = []

for name in sr:
    full_list.append(list(name))

print(full_list)

totName = 0

for name in full_list:
    for character in name:
        totName += ord(character)
        print(ord(character))
print(totName)
print(chr(totName))



color('red', 'yellow')
begin_fill()
for name in full_list:
    forward(start)
    for character in name:
        forward(stop)
        left(ord(character)*2)
end_fill()
done()
print('done')

