# print(' '*4 + '* '*1)
# print(' '*3 + '* '*2)
# print(' '*2 + '* '*3)
# print(' '*1 + '* '*4)
# print(' '*0 + '* '*5)

# for i in range(5):
#     print(' '*(5-i-1) + '* '*(i+1))

# number = int(input("How many starts do you want? "))
# for i in range(number):
#     print(' '*(number-i-1) + '* '*(i+1))
######################################################

# for i in range(5):
#     print(' ' * i + '* '*(5-i))

# number = int(input("how many numbers do you want? "))
# for i in range(number):
#     print(' ' * i + '* '*(number-i))
#####################################################
# j = 7
# for i in range(j):
#     if i > j/2:
#         print('* ' * (j-i))
#     else:
#         print('* ' * (i+1))


number = int(input("how many starts do you want? "))
j = number
if number % 2 == 0:
    j += 1
for i in range(j):  # i = 0
    if i > j/2:
        print('* ' * (j-i))

    else:
        print('* ' * (i+1))
