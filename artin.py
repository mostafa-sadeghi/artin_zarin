# string = "He said, \"Aren't can't shouldn't wouldn't.\""

# myscore = 1000
# message = 'i scored % s' % myscore
# print(message)


# name = "ali"
# family = "mohamadi"
# message = "hello %s %s" % (name, family)
# print(message)


# name = "ali"
# family = "mohamadi"
# message = f"hello {name} {family}"
# print(message)


# myscore = 1000
# message = f'i scored {myscore}'
# print(message)


# string = "abcd"  # immutable
# for i in range(len(string)):
#     print(string[i])


# a = "*" * 5

# print(a)

# number = int(input("enter your selection: "))
# for i in range(number, 0, -1):
#     print(i * "*")


# shopping_list = ["egg", "tomato", "potato", 1, [""]]
# shopping_list[0] = "milk"
# for item in shopping_list:
#     print(item)

# print(shopping_list[:2])


# numbers = [1, 2, 3, 4, 5, 6]

# odd_numbers = numbers[1:4:2]
# new_list = [numbers, odd_numbers]
# print(new_list)
# print(new_list[0][0])


# numbers = [1, 2, 3, 4, 5, 6]
# numbers.append(7)
# print(numbers)
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.insert(0, 0)
# print(numbers)
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.remove(6)
# print(numbers)
# numbers = [1, 2, 3, 4, 5, 6]
# del numbers[-1]
# print(numbers)
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.pop()
# print(numbers)
# numbers = [1, 2, 3, 4, 5, 6]  # mutable
# numbers[0] = "b"
# print(numbers)
# numbers = (1, 2, 3, 4, 5, 6)  # immutable
# string = 'hello world'
# string[1] = '*'

# numbers = [1, 2, 3, 4, 5, 6]

# for index, value in enumerate(numbers):
#     print(index, value)


# for item in numbers:
#     print(item)


# numbers = [1, 2, 3, 4, 5, 6]

# i = 0
# while i < len(numbers):
#     print(i, numbers[i])
#     i += 1  # i = i + 1


# numbers = list(range(0, 1001, 2))

# print(f'there is {len(numbers) -1 } even numbers between 0 and 1000')
# print(f'sum of all even numbers is : {sum(numbers)}')

# numbers = list(range(1, 1001))
# even_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(f'there is {len(even_numbers) } even numbers between 0 and 1000')
# print(f'sum of all even numbers is : {sum(even_numbers)}')

# x = list(range(1, 5, 2))

# print(x)


# import random
# from decimal import Decimal
# x = ["milk", "potato", "tomato"]

# for i in x:  # i = potato
#     if i == 'tomato':
#         print("there is tomato in build list")
#     else:
#         print("ther is no tomato in our list")

# i = 0
# while i < len(x):
#     if x[i] == "potato":
#         print("there is tomato in our list")
#         break
#     i += 1  # i = i + 1

# grades = [19, 20, 20, 18, 17, 16, 15, 14, 19]
# name = input("enter your name > ")
# family = input("enter your family:> ")

# total = sum(grades)
# average = total/len(grades)

# print(f'average is {average:.2f}')

# for item in range(100):
#     print(item)

# numbers = list(range(1, 100, 2))
# print(numbers)

# x = 1

# y = float(x)

# print(y)


# average = Decimal('19.5')
# print(average, type(average))

# x = float(2.5)
# print(f'{x:.40f}')


# for i in range(100):
#     if i == 10:
#         continue
#     print(i)


# gender = "Female"
# age = 70

# if gender == "Male" or age >= 65:
#     print("he is old")


# if 1 == 1 and 1 == 3:
#     print("ok")


# if 1 > 3 and 1 > 0 and 3==3:  # short circuit in and operator
#     print('ok')


# if "a" == "a" or 1 == 2:  # short circuit in or operator
#     print('ok')


# x = True

# print(not(x))


# grade = 88

# if not grade == 87:
#     print('ok')

# def my_function(number):  # define a function
#     number * 2


# number = int(input("enter your number> "))
# print(my_function(number))  # calling a function
# x = my_function(number)   # calling a function
# print(x)


# x = "ali"
# y = "rezaei"
# age = 10


# def show_info(name, family, age):
#     return f'{name} {family} is {age} years old'


# print(show_info(x, y, age))


# def maximum(x, y, z):

#     max_value = x
#     if y > max_value:
#         max_value = y
#     if z > max_value:
#         max_value = z
#     return f'max_value between {x} and {y} and {z} is : {max_value}'


# print(maximum(1, 2, 3))

# x = [1, 2, 3]

# maximum = max(x)

# print(f'maximum number is: {maximum}')


# for roll in range(10):
#     face = random.randrange(1, 7)
#     print(face, end="  ")

# import random
# frequency1 = 0
# frequency2 = 0
# frequency3 = 0
# frequency4 = 0
# frequency5 = 0
# frequency6 = 0

# for roll in range(6_000_000):
#     face = random.randrange(1, 7)

#     if face == 1:
#         frequency1 += 1  # frequency1 = frequency1 + 1
#     elif face == 2:
#         frequency2 += 1
#     elif face == 3:
#         frequency3 += 1
#     elif face == 4:
#         frequency4 += 1
#     elif face == 5:
#         frequency5 += 1
#     elif face == 6:
#         frequency6 += 1


# print(f'Face{"Frequencies":>14}')
# print(f'{1:>4}{frequency1:>14,}')
# print(f'{2:>4}{frequency2:>14,}')
# print(f'{3:>4}{frequency3:>14,}')
# print(f'{4:>4}{frequency4:>14,}')
# print(f'{5:>4}{frequency5:>14,}')
# print(f'{6:>4}{frequency6:>14,}')
