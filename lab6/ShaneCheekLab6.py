__author__ = "Shane Cheek"

# Description:
#     This program will represent a dog park. It will allow
#     dogs to come and go in and out of the dog park. New
#     dogs can be added and removed from the dog park. The
#     dogs will have different levels of obedience. This may
#     lead to dog fights!!!


# Input
#     dog name:  to be added or removed from the dog park
#     This will instantiate a new dog or destroy a instance
#     of the dog named by the user (input).


# Output:
#     dog.__owner, dog_name, commands

# Declare Dict dogInstanceList
dogInstanceList = {}


# class Dog
#     Private String __name
#     Private String __owner
# 
#     Public Module setter()
#         Set __name = name
#         Set __owner = owner
#     End Module
# 
#     Public Function dog_name_getter()
#         return __name
#     End Function
# 
#     Public Function  owner_name_getter()
#         return __owner
#     End Function
# 
#     Public Module add_dog():
#         dog_name = input('Name of the dog. ').lower()
#         if not check_dog_in_park:
#             print('This dog is already in the dog park.')
#         else:
#             setter(dog_name, input('Owner of the dog. ', ).lower())
#             dogInstanceList[dog_name] = self
#             print(dog_name.title(), 'has entered the dog park. Have fun buddy!')
#     End Module


class Dog:
    __name = ''
    __owner = ''

    def setter(self, name, owner):
        self.__name = name
        self.__owner = owner

    def dog_name_getter(self):
        return self.__name

    def owner_name_getter(self):
        return self.__owner

    # I think this really should be in an instance of a dog park, along with print_dog() and remove_dog().
    def add_dog(self):
        dog_name = input('Name of the dog. ').lower()
        if not check_dog_in_park:
            print('This dog is already in the dog park.')
        else:
            self.setter(dog_name, input('Owner of the dog. ', ).lower())
            dogInstanceList[dog_name] = self
            print(dog_name.title(), 'has entered the dog park. Have fun buddy!')


# Module print_dog()
#     If Call are_dogs()
#         Display('The dog/s in the dog park are:')
#         For dog in dogInstanceList
#             Display('\t' + Call dogInstanceList[dog].dog_name_getter().title())
# End Module 

def print_dog():
    if are_dogs():
        print('The dog/s in the dog park are:')
        for dog in dogInstanceList:
            print('\t' + dogInstanceList[dog].dog_name_getter().title())


#
# Function Bool check_dog_in_park(String dog_name)
#     If dog_name in dogInstanceList
#         Return True
# End Function

def check_dog_in_park(dog_name):
    if dog_name in dogInstanceList:
        return True


# Module are_dogs()
#     If len(dogInstanceList) > 0:
#         Return True
#     Else:
#         Display There are no dogs in the dog park.
# End Module

def are_dogs():
    if len(dogInstanceList) > 0:
        return True
    else:
        print('There are no dogs in the dog park.')


# Module remove_dog()
#     If True:
#         name = Input('Name the dog you want to remove from the park. ')
#         Try:
#             Del dogInstanceList[name]
#             Display name, has been removed.
#             Call print_dog()
#         Except ValueError:
#             Display name, is not in the dog park.
# End Module

def remove_dog():
    if are_dogs():
        name = input('Name the dog you want to remove from the park. ')
        try:
            del dogInstanceList[name]
            print(name.title(), 'has been removed.')
            print_dog()
        except ValueError:
            print(str(name).title(), 'is not in the dog park.')


#
# Module dog_owner()
#     If True:
#         dog_name = Input('Name the dog you want to know the owner of. ')
#         Try:
#             Display(dog_name + '\'s', 'owner is', dogInstanceList[dog_name].owner_name_getter())
#         except KeyError:
#             Display(str(dog_name).title(), 'is not in the dog park.')
# End Module

def dog_owner():
    if are_dogs():
        dog_name = input('Name the dog you want to know the owner of. ')
        try:
            print(dog_name + '\'s', 'owner is', dogInstanceList[dog_name].owner_name_getter())
        except KeyError:
            print(str(dog_name).title(), 'is not in the dog park.')


# Function String options_list( String commands='')
#     Declare options
#     Set options = {
#         'add': 'Add a dog to the dog park.',
#         'remove': 'Remove a dog from the dog park.',
#         'print': 'Print all dogs in the dog park.',
#         'quit': 'Quit the program',
#         'owner': 'Check the owner of a dog',
#         'options': 'Get your options'
#     }
#     If commands not in options
#         print('Your options are:')
#         For option, instruction in options.items():
#             Display '\t' + option + ':', instruction
#     Else If commands in options
#         Return commands
# End Function

def options_list(commands=''):
    options = {}
    options = {
        'add': 'Add a dog to the dog park.',
        'remove': 'Remove a dog from the dog park.',
        'print': 'Print all dogs in the dog park.',
        'quit': 'Quit the program',
        'owner': 'Check the owner of a dog',
        'options': 'Get your options'
    }
    if commands not in options:
        print('Your options are:')
        for option, instruction in options.items():
            print('\t' + option + ':', instruction)
    elif commands in options:
        return commands


# Module command_option()
#     Declare user_select_option
#     user_select_option = input('\nWhat would you like to do?\n').lower()
#     If options_list(user_select_option)
#         Return user_select_option
# End Module

def command_option():
    user_select_option = ''
    user_select_option = input('\nWhat would you like to do?\n').lower()
    if options_list(user_select_option):
        return user_select_option


# Module intro()
#     Display 'You are the dog park monitor.\nYou must add and remove dogs to the dog park list as they come and go.\n'
# End Module
def intro():
    print('You are the dog park monitor.\nYou must add and remove dogs to the dog park list as they come and go.\n')


# Module main()
#     Call intro()
#     Call options_list()
#     Declare command = ''
#
#     While True
#         Set command = command_option()
# 
#         If command == 'quit'
#             break
#         Else If command = 'print'
#             Call print_dog()
# 
#         Else If command = 'add'
#             Declare new_dog
#             Set new_dog = Dog()
#             Call new_dog.add_dog()
# 
#         Else If command = 'remove'
#             Call remove_dog()
# 
#         Else If command = 'owner'
#             Call dog_owner()
# 
#         Else If command = 'options'
#             Call options_list()
#       End While
# End Module

def main():
    intro()
    options_list()
    command = ''
    while True:
        command = command_option()

        if command == 'quit':
            break
        elif command == 'print':
            print_dog()

        elif command == 'add':
            new_dog = None
            new_dog = Dog()
            new_dog.add_dog()

        elif command == 'remove':
            remove_dog()

        elif command == 'owner':
            dog_owner()

        elif command == 'options':
            options_list()


# Call main()
main()
