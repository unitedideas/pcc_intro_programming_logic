import time

start = time.time()

name_list = []

name = input('name')

sr = list(name)

for character in sr:
    print(ord(character))

stop = time.time()

print(round(stop - start, 2))
