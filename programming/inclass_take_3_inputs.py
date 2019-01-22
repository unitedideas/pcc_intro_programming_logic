__author__ = 'Shane Cheek'
# description:
# calculate the score of a student for 3 assignments

# inputs:
# score1, score2, score3

# output:
# display the sums of the 3 inputs
# display the % score

# process:
# add inputs as they aer entered

# declare variables:
list_of_assignments = []
score = 0.0
percent = 0.0
maxScore = 0
list_of_assignments = {'homework 1, max is 10 points.': 10, 'homework 2, max is 20 points.': 20,
                       'quiz 1, max is 10 points.': 10}
for score in list_of_assignments:
    maxScore += list_of_assignments[score]
while True:
    try:
        for assignment in list_of_assignments:
            score = float(input('Tell me you score for ' + str(assignment) + ': '))
            score += score
        break
    except TypeError:
        "You did not enter a number. Starting over..."

percent = score / maxScore
print('Your score is ' + str(score) + ' of ' + str(maxScore), 'You scored a ' + str(percent) + '%')
