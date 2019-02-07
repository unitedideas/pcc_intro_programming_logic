# Author: Shane Cheek
# Date: Feb 6th 2019

# input
numOfHours = int(input('Provide a number of hours'))

# calc
days = numOfHours // 24
hours = numOfHours - (days * 24)

# output
print('That is', days,'and', hours, 'hours')
