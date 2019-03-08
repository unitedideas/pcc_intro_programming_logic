# # 10 and 11
# counter = 1
# while counter < 10:
#     counter += 1
#     print(counter)

#
# def halve(n):
#     half = int(n) / 2
#     return int(half)
#
#
# def log2(n):
#     lg2 = 0
#     while n > 1:
#         n = halve(n)
#         lg2 = lg2 + 1
#     return lg2
#
#
#
# print(log2(8))
# print(log2(4))
# print(log2(1))
# print(log2(13))

#
# def perfect(n):
#     count = 0
#     sum = 0
#
#     while count < n:
#         count = count + 1
#         sum = sum + count
#
#     return sum
#
#
# def perfect_sum(n):
#     count = 0
#     sum = 0
#
#     while count < n:
#         count = count + 1
#         sum = sum + perfect(count)
#     return sum
#
#
# def main():
#     print(perfect_sum(5))


# def loop_rule(n):
#     if n % 2 == 0:
#         n = n / 2
#     else:
#         n = n * 3 + 1
#     print(n)
#     return n
#
#
# def loop(n):
#     count = 0
#     while n != 1:
#         count = count + 1
#         n = loop_rule(n)
#     return count
#
#
# print(loop(3))
#

# def fibo(n):
#     first = 1
#     second = 1
#     next = 0
#     counter = 0
#
#     while counter < n:
#         counter = counter + 1
#         next = first + second
#         first = second
#         second = next
#         print(next)
#
# fibo(5)


# def fibo_2(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibo_2(n - 1) + fibo_2(n - 2)
#
#
# def loop(n):
#     counter = 0
#
#     while counter < n:
#         counter = counter + 1
#         print(fibo_2(counter))
#
# loop(6)
#
# boollist = [0, None, False, True]
# for name in boollist:
#     print(type(name))

# print(18.5/25)
