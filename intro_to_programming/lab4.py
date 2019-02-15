__author__ = 'Shane Cheek'


# Description:
# Program helps decide what to do if you have unopened mail or junk mail after validation of the input.

# inputs: is_more_mail, junk_or_not

# outputs: output_relax(), junk_mail()

# Module is_more_mail()
#     Declare String is_more_mail
#     Display Do you have mail?
#     Input is_more_mail
#     If is_more_mail == 'y' Then
#         Call output_get_next_mail()
#         Call junk_mail()
#     Else
#         Call output_relax()
# End Module

# function Boolean is_valid_answer(String answer)
#     is_valid = answer a valid string (y or n)
#     Return is_valid
# End Function

def is_valid(answer):
    answer = answer.lower()
    try:
        answer == 'y' or answer == 'n'
        return answer
    except ValueError:
        is_valid = False
        return is_valid


# Module output_get_next_mail()
#     Display 'Get the next piece of mail.'

# Module junk_mail()
#     Declare String junk_or_not = ''
#     Display 'Is it junk mail?'
#     Input junk_or_not
#
#     If junk_or_not == 'y'
#         Display 'Throw it away!'
#     Else
#         Display 'Open it and read it.'
# End Module

# Module output_relax()
#     Display 'Go do your Intro to Programming Logic homework'
# End Module

# Module main()
#     Call is_more_mail()
# End Module

def output_get_next_mail():
    print('Get the next piece of mail.')


def junk_mail():
    junk_or_not = ''
    junk_or_not = input('Is it junk mail?')

    if junk_or_not == 'y':
        print('Throw it away!')
    else:
        print('Open it and read it.')


def output_relax():
    print('Go do your Intro to Programming Logic homework')


def is_more_mail():
    is_more_mail = ''
    is_more_mail = is_valid(input('Do you have mail?'))
    if is_more_mail == 'y':
        output_get_next_mail()
        junk_mail()
    else:
        output_relax()


def main():
    is_more_mail()


if __name__ == '__main__':
    main()
