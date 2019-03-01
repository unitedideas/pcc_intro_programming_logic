__author__ = 'Shane Cheek'

'''
Description:
    Program helps decide what to do if you have unopened mail
    and/or if that mail is junk mail.
'''

'''
inputs:
    is_more_mail, junk_or_not
'''

'''
outputs:
    relax(), junk_mail()
'''

'''
Module junk_mail():
    Declare String junk_or_not = ''
    Set String junk_or_not = input('Is it junk mail?')
    While junk_or_not is not 'no' AND junk_or_not is not 'yes':
        Set String junk_or_not = input('Is it junk mail?')
    If junk_or_not == 'yes':
        Display 'Throw it away!'
    Else:
        Display 'Open it and read it.'


Module relax():
    Display 'Go do your Intro to Programming Logic homework'


Function Bool is_more_mail():
    Declare String have_mail = ''
    Set String have_mail = input('Do you have mail?')
    While have_mail is not 'no' and have_mail is not 'yes':
        Set String have_mail = input('Do you have mail?')
    If have_mail == 'yes':
        Call junk_mail()
        Return True


Module main():
    Declare have_mail = ''
    Set Bool have_mail = True
    While have_mail is True:
        Set have_mail = is_more_mail()
    Call relax()
'''


def junk_mail():
    junk_or_not = ''
    junk_or_not = input('Is it junk mail?')
    while junk_or_not != 'no' and junk_or_not != 'yes':
        junk_or_not = input('Is it junk mail?')
    if junk_or_not == 'yes':
        print('Throw it away!')
    else:
        print('Open it and read it.')


def relax():
    print('Go do your Intro to Programming Logic homework')


def is_more_mail():
    have_mail = input('Do you have mail?')
    while have_mail != 'no' and have_mail != 'yes':
        have_mail = input('Do you have mail?')
    if have_mail == 'yes':
        junk_mail()
        return True


def main():
    have_mail = ''
    have_mail = True
    while have_mail:
        have_mail = is_more_mail()
    relax()


if __name__ == '__main__':
    main()
