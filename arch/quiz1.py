

# def input_age():
#     age = 0
#     age = input("Please enter your age: ")
#     return age
#
# def calculate_magic(age):
#     result = 0
#     temp = 0
#     age= int(age)
#
#     temp = age
#
#     result = age * 2
#
#     result = int(result) + 10
#
#     result = result / 2
#
#     result = result - temp
#
#     return result
# def output_result(result):
#     print(result)
#
# def main():
#     age = 0
#     result = 0
#
#
#     age = input_age()
#
#     result = calculate_magic(age)
#
#     output_result(result)
#
#
# main()


#
# a = "1.0"
# b = '2.0'
# c = '3.0'
#
# a = b
# b = c
# c = a
# d = a + b + c
#
# print(d)
#
#
#


# 
# def double(x):
#     d = x + x
#     return d
# 
# def  triple_double(x):
#     t = double(x) + double(x) + double(x)
#     return t
# 
# def main():
#     result = double(triple_double(1.0))
#     print(result)
# 
# 
# if __name__ == '__main__':
#     main()



# 
# def initialize(y):
#     x = y
#     output(x)
#     output(y)
# 
# def output(x):
#     print(x)
# 
# def main():
#     x = 0.0
#     y = 2.0
# 
#     output(x)
#     output(y)
#     initialize(y)
#     output(x)
#     output(y)
# 
# 
# 
# if __name__ == '__main__':
#     main()
# 
# 



# def output_results(fair_dollars_per_gallon, actual_dollars_per_gallon, price_gouge):
#     print("The fair price for a gallon of gas is", fair_dollars_per_gallon)
#     print("Your actual price for a gallon of gas is", actual_dollars_per_gallon)
#     print("You are being overcharged by", price_gouge, "per gallon!")
#
#
# def calculate_fair_dollars_per_gallon(dollars_per_barrel):
#     GALLONS_OF_GAS_PER_BARREL_OF_OIL = 19.0
#     fair_dollars_per_gallon = dollars_per_barrel / GALLONS_OF_GAS_PER_BARREL_OF_OIL
#     return fair_dollars_per_gallon
#
#
# def input_values():
#     dollars_per_barrel = input("What is the current cost of a barrel of oil?")
#     actual_dollars_per_gallon = input("What is the actual cost of a gallon of gas?")
#     return dollars_per_barrel, actual_dollars_per_gallon
#
#
# def calculate_price_gouge(actual_dollars_per_gallon, fair_dollars_per_gallon):
#     price_gouge = actual_dollars_per_gallon - fair_dollars_per_gallon
#     return price_gouge
#
#
# def main():
#     dollars_per_barrel = 0.0
#     actual_dollars_per_gallon = 0.0
#     fair_dollars_per_gallon = 0.0
#
#     price_gouge = 0.0
#
#     input_values()
#
#     calculate_fair_dollars_per_gallon(dollars_per_barrel)
#
#     calculate_price_gouge(actual_dollars_per_gallon, fair_dollars_per_gallon)
#
#     output_results(fair_dollars_per_gallon, actual_dollars_per_gallon, price_gouge)
#
#
# if __name__ == '__main__':
#     main()

#
# GALLONS_OF_GAS_PER_BARREL_OF_OIL = 19.0
#
# dollars_per_barrel = 44.46
#
# actual_dollars_per_gallon = 2.79
#
# fair_dollars_per_gallon = dollars_per_barrel / GALLONS_OF_GAS_PER_BARREL_OF_OIL
#
# price_gouge = actual_dollars_per_gallon - fair_dollars_per_gallon
#
#
# print(fair_dollars_per_gallon)
#
# print(price_gouge)
#
