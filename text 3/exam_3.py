# # question 9
# def average(values, size):
#     total = 0.0
#     counter = 0
#     while counter < size:
#         total = total + values[counter]
#         counter = counter + 1
#     return total / size
#
#
# scores = [90, 80, 70, 100, 60, 80]
# print(average(scores, 6))
#
# #  output 80.0

#
# #question 10
# def getScore(student, names, scores, size):
#     counter = 0
#
#     while counter < size:
#         if student == names[counter]:
#             return scores[counter]
#         counter = counter + 1
#     return -1
#
#
# names = ["John", "Paul", "George", "Ringo", "Pete"]
# scores = [100, 80, 90, 70, 50]
#
# print(getScore("George", names, scores, 5))
# #  output 90

# # question 11
# def getStats(scores, size):
#     counter = 0
#     min = 100
#     max = 0
#     total = 0
#
#     while counter < size:
#         if scores[counter] > max:
#             max = scores[counter]
#         if scores[counter] < min:
#             min = scores[counter]
#         total = total + scores[counter]
#         counter = counter + 1
#     print(min, max, total / counter)
#     #  output
#
# scores = [100, 80, 90, 70, 50]
#
# getStats(scores, 5)
#
# # output 50 100 78.0


# # Question 12
# def fibo(n):
#     vals = [1,1,1,1,1,1,1,1]
#     counter = 2
#     while counter < n:
#         vals[counter] = vals[counter - 1] + vals[counter - 2]
#         counter += 1
#     return vals
#
#
# def output_vals(vals, n):
#     counter = 0
#
#     while counter < n:
#         print(vals[counter], end= " ")
#         counter += 1
#
#
# def main(n):
#     vals = fibo(n)
#     output_vals(vals, n)
#
#
# main(8)
# # output 1 1 2 3 5 8 13 21


# # Question 13
# class Coordinate:
#
#     def set_x(self, value):
#         self._x = value
#
#     def set_y(self, value):
#         self._y = value
#
#     def get_x(self):
#         return self._x
#
#     def get_y(self):
#         return self._y
#
#     def add(self, c):
#         self._x = self._x + c.get_x()
#         self._y = self._y + c.get_y()
#
#
# def main():
#     c1 = Coordinate()
#     c2 = Coordinate()
#
#     c1.set_x(1.0)
#     c1.set_y(2.0)
#     c2.set_x(3.0)
#     c2.set_y(4.0)
#
#     print(c1.get_x(), c1.get_y(), c2.get_x(), c2.get_y())
#
#     c1.add(c2)
#
#     print(c1.get_x(), c1.get_y(), c2.get_x(), c2.get_y())
#
# main()
#
# # output 1.0 2.0 3.0 4.0
# # 4.0 6.0 3.0 4.0


# #  Question 14
# class Animal:
#     def setName(self, name):
#         self._name = name
# 
#     def vocalize(self):
#         print(self._name + " makes a noise.")
# 
# 
# class Dog(Animal):
#     def vocalize(self):
#         print(self._name + " woofs.")
# 
# 
# class Cat(Animal):
#     def vocalize(self):
#         print(self._name + " meows.")
# 
# 
# class Bird(Animal):
#     def vocalize(self):
#         print(self._name + " chirps.")
# 
# 
# def main():
#     pets = [1, 1, 1]
#     counter = 0
# 
#     pets[0] = Dog()
#     pets[1] = Cat()
#     pets[2] = Bird()
#     pets[0].setName("Dorothy")
#     pets[1].setName("Ginger")
#     pets[2].setName("Ralph")
#     while counter < 3:
#         pets[counter].vocalize()
#         counter = counter + 1
# 
# 
# main()
# # output
# # Dorothy woofs.
# # Ginger meows.
# # Ralph chirps.
# 
# 
# #  Question 15
# class Musician:
#     def __init__(self, name, rating, song):
#         self._name = name
#         self._rating = rating
#         self._song = song
# 
#     def display(self):
#         print(self._name, self._rating, self._song)
# 
#     def matches(self, name):
#         return name == self._name
# 
# 
# def main(name):
#     musicians = [1, 1, 1, 1]
#     counter = 0
# 
#     musicians[0] = Musician("John", 10, "Imagine")
#     musicians[1] = Musician("Paul", 9, "Listen to What the Man Said")
#     musicians[2] = Musician("George", 8, "Here Comes the Sun")
#     musicians[3] = Musician("Ringo", 7, "With a Little Help From My Friends")
# 
#     while counter < 4:
#         if musicians[counter].matches(name):
#             musicians[counter].display()
#         counter = counter + 1
# 
# 
# main("George")
# # output George 8 Here Comes the Sun

# # Question 16
# class Material:
#     def __init__(self, type):
#         self._type = type
#
#     def display(self):
#         print(self._type)
#
#
# class Furniture:
#     def set_material(self, material):
#         self._material = material
#
#     def display(self):
#         print(self._type)
#         self._material.display()
#
#
# class Chair(Furniture):
#     def Chair(self):
#         self._type = "Chair"
#
#
# def main():
#     furniture = Chair()
#
#     furniture.set_material(Material("Wood"))
#     furniture.display()
#
# main()
# # Output Wood Chair
