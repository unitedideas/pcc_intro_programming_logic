# Author: Shane Cheek
# Date: Feb 6th 2019

# input
ppt = float(input('Provide a real number (decimal) eg. 1.50; Price per ticket'))
day1 = int(input('How many tickets needed on day 1.'))
day2 = int(input('How many tickets needed on day 2.'))

# calc
total = (ppt * day1)
total += (ppt * day2)


# output
print('Total ticket price is', total,)
