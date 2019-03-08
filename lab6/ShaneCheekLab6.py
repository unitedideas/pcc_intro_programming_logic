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


dogInstanceList = {}


class Dog:
    # def __init__(self, name='unknown', owner='unknown'):
    #     self.__name = name
    #     self.__owner = owner

    def setter(self, name, owner='unknown'):
        self.__name = name
        self.__owner = owner

    def dog_name_getter(self):
        return self.__name

    def owner_name_getter(self):
        return self.__owner


def handle_dog_instance_list(name):
    dogInstanceList[name] = name
    print(name, dogInstanceList[name, name])


def print_dog():
    if len(dogInstanceList) > 0:
        print('The dog/s in the dog park are:')
        for dog in dogInstanceList:
            print(dogInstanceList[dog].dog_name_getter().title())
        return True
    else:
        print('There are no dogs in the dog park.')
        return False


def add_dog():
    dog_name = input('Name of the dog. ').lower()
    if dog_name in dogInstanceList:
        print('This dog is already in the dog park.')
    else:
        new_dog = Dog()
        new_dog.setter(dog_name, input('Owner of the dog. ', ).lower())
        dogInstanceList[dog_name] = new_dog
        print(dog_name.title(), 'has entered the dog park. Have fun buddy!')


def remove_dog():
    if print_dog():
        name = input('Name the dog you want to remove from the park. ')
        try:
            del dogInstanceList[name]
            print(name.title(), 'has been removed.')
            print_dog()
        except ValueError:
            print(str(name).title(), 'is not in the dog park ')


def dog_owner():
    if print_dog():
        dog_name = input('Name the dog you want to know the owner of. ')
        try:
            print(dog_name + '\'s', 'owner is', dogInstanceList[dog_name].owner_name_getter())
        except KeyError:
            print(str(dog_name).title(), 'is not in the dog park ')


def options_list(command=False):
    options = {
        'add': 'Add a dog to the dog park.',
        'remove': 'Remove a dog from the dog park.',
        'print': 'Print all dogs in the dog park.',
        'quit': 'Quit the program',
        'owner': 'Check the owner of a dog',
        'options': 'Get your options'
    }
    if not command:
        print('Your options are:')
        for option, instruction in options.items():
            print(option + ':', instruction)
    elif command in options:
        print(options[command])
        return command


def command_option():
    user_select_option = input('\nWhat would you like to do?\n').lower()
    if options_list(user_select_option):
        return user_select_option

options_list()

while True:
    command = command_option()

    if command == 'quit':
        break
    elif command == 'print':
        print_dog()

    elif command == 'add':
        add_dog()

    elif command == 'remove':
        remove_dog()

    elif command == 'owner':
        dog_owner()

    elif command == 'options':
        options_list()
