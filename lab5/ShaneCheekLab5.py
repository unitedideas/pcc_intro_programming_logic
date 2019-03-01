import time

start = time.time()


name = input('name')

sr = list(name)

totName = 0
for character in sr:
    totName+=ord(character)
    print(ord(character))
print(totName)
print(chr(totName))

stop = time.time()

print(round(stop - start, 2))
