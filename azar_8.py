# string = input('enter e sequence of numbers: (Example:1,2,3,4) ')
# result = 0
# numbers = string.split(',')
# string_output = ''
# for s in numbers:
#     result += int(s)
# print(f'sum of {len(numbers)} numbers is : {result}')


# Exercise 2:
#
'''Write a program that asks the user to input 10 integers,
and then prints the largest odd number that was entered.
If no odd number was entered, it should print a message to that effect'''


# x = list(range(10))
# print(x)

# largest_odd_number = 0
# for i in range(10):
#     number = int(input('> '))
#     if number % 2 != 0 and number > largest_odd_number:
#         largest_odd_number = number

# if largest_odd_number == 0:
#     print('you enterd no odd number')
# else:
#     print(f'biggest odd number is: {largest_odd_number}')

# exercise : write above code with while loop

# i = 0
# largest_odd_number = 0
# while i < 10:
#     number = int(input('> '))
#     if number % 2 != 0 and number > largest_odd_number:
#         largest_odd_number = number
#     i = i + 1  # i +=1

# if largest_odd_number == 0:
#     print('you enterd no odd number')
# else:
#     print(f'biggest odd number is: {largest_odd_number}')

# exercise :
'''Write a program that examines three variables—x, y, and z—and prints the largest
odd number among them. If none of them are odd, it should print a message to that effect'''

# x = int(input('enter number one:> '))
# y = int(input('enter number two:> '))
# z = int(input('enter number three:> '))

# if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
#     print('all numbers are even!!!')
# elif x % 2 == 0 and y % 2 == 0:
#     print(z)
# elif x % 2 == 0 and z % 2 == 0:
#     print(y)
# elif y % 2 == 0 and z % 2 == 0:
#     print(x)
# elif x % 2 == 0:
#     if y > z:
#         print(y)
#     else:
#         print(z)
# elif y % 2 == 0:
#     if x > z:
#         print(x)
#     else:
#         print(z)
# elif z % 2 == 0:
#     if x > y:
#         print(x)
#     else:
#         print(y)
# else:
#     if x > y and x > z:
#         print(x)
#     elif y > z:
#         print(y)
#     else:
#         print(z)


# exercise : یک عدد از ورودی بگیر و به اون تعداد * رو به خودش بچسبان

# star = int(input('enter how many star numbers you want> '))
# print(star * '*')

# star = int(input('enter how many star numbers you want> '))
# result = ''
# for i in range(star):
#     result += '*'

# print(result)


# exercise:
'''
write a loop to do like this:
Enter string 1/5: the blue moon
Enter string 2/5: the red guitar
Enter string 3/5: go home
Enter string 4/5: spill the beans
Enter string 5/5: winter in Oklahoma


write another loop to show entered strings reverse like this:

String 5/5: winter in Oklahoma
String 4/5: spill the beans
String 3/5: go home
String 2/5: the red guitar
String 1/5: the blue moon
'''
