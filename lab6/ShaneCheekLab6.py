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


class Dog:
    def __init__(self, _name, _age, _owner):
        self._name = _name
        self._age = _age
        self._owner = _owner

    def __del__(self):
        print('Removed', self._name, 'from the dog park. Bye Bye', self._name)


dogInstanceList = ['shane']


def handleDogInstanceList(name):
    dogInstanceList.append(name)


# def set_name(self):
#     self._name = _name

# def handleQuitCommand(command):
#     if command == 'quit':
#         return break

options = ['add', 'remove', 'print', 'quit']

while True:
    command = input('What would you like to do? Add, Remove, Print, Quit ').lower()

    if command in options:
        if command == 'quit':
            break
        elif command == 'print':
            if len(dogInstanceList) > 0:
                for dog in dogInstanceList:
                    print(dog)
            else:
                print('There are no dogs in the dog park.')

        elif command == 'add':
            name = input('name').lower()
            name = Dog(name, input('age').lower())
            print(name._name, name._age)
            handleDogInstanceList(name._name)

        elif command == 'remove':
            name = input('Name the dog you want to remove from the park. ')
            try:
                del locals()[name]
                dogInstanceList.remove(name)
                print('Remaining Dog ' + str(dogInstanceList))
            except KeyError:
                print(str(name).title(), 'is not in the dog park ')
