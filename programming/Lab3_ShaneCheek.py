__author__ = 'Shane Cheek'

# Description:
# Program helps decide what to do if you have unopened mail or junk mail.

# inputs:
#   more_mail, is_it_junk_mail

# outputs:
#   open_mail, relax


# Module main()
#
#
#
#
# End Module

# Module output_relax()
#   Display 'Go Relax.'

# Module output_get_next_mail()
#   Display 'Get the next letter.'

# Function Bool input_is_more_mail()
#   Declare Bool more_mail
#   Display 'Is there more unopened mail?'
#   Input more_mail
#   Return more_mail
# End Function


# Module Bool input_scores(list_of_assignments)
#   declare percent_score

# Function calc_percent(score, max_score)
#   declare percent_score

# End Module
#####

def display_score(score, max_score, percent):
    print('Your score is ' + str(score) + ' of ' + str(max_score), 'You scored a ' + str(percent) + '%')


def maxScore(assignments):
    max_score = 0
    for assignment in assignments:
        max_score += assignments[assignment]
    return max_score


def input_scores(list_of_assignments):
    while True:
        try:
            score = 0
            for assignment in list_of_assignments:
                score += float(input('Tell me you score for ' + str(assignment) + ': '))
            break
        except ValueError:
            "You did not enter a number. Starting over..."
    return score


def calc_percent(score, max_score):
    percent_score = (score / max_score) * 100.00
    return percent_score


def main():
    # declare variables:
    list_of_assignments = []
    score = 0.0
    percent_score = 0.0
    max_score = 0
    list_of_assignments = {'homework 1, max is 10 points.': 10, 'homework 2, max is 20 points.': 20,
                           'quiz 1, max is 10 points.': 10}

    # calculate the max possible score
    max_score = maxScore(list_of_assignments)

    # calculate student total score
    score = input_scores(list_of_assignments)

    # calculate the percent
    percent_score = calc_percent(score, max_score)

    # display the total score, max score and the percent
    display_score(score, max_score, percent_score)


if __name__ == '__main__':
    main()

