# Sample String : 'The sara is not that poor!'
# 'The sara is poor!'
# Expected Result : 'The sara is good!'
# 'The sara is poor!'


# def not_poor(string):
#     snot = string.find('not')
#     spoor = string.find('poor')

#     if spoor > snot and snot > 0 and spoor > 0:
#         string = string.replace(string[snot:spoor+4], "good")
#         return string
#     else:
#         return string


# output = not_poor('The sara is not that poor!')
# output = not_poor('The sara is poor!')
# print(output)


# string = "good"

# print("good".find("o"))

# def largest_string(world_list):
#     output_list = []
#     for word in world_list:
#         output_list.append((len(word), word))

#     output_list.sort()

#     return output_list[-1][0], output_list[-1][1]


# z = largest_string(["good", "very very very bad", "very good"])
# print(z)


# def remove_index_char(string, index):
#     part1 = string[:index]
#     part2 = string[index+1:]

#     return part1 + part2


# output = remove_index_char("python", 0)
# print(output)


import random


def roll_dice():
    '''
    This Function is used for rolling two dice
    Returns: Tuple
    '''
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)

    return (die1, die2)


def display_dice(dice):
    die1, die2 = dice
    print(f"player rolled {die1} + {die2} = {sum(dice)}")


# first roll
print('first roll!!!!')
player_name = input('Enter your name: ')
die_value = roll_dice()
display_dice(die_value)

# sum_of_dice = die_value[0] + die_value[1]
# print(sum_of_dice)


sum_of_dice = sum(die_value)

# if sum_of_dice == 7 or sum_of_dice == 11:
if sum_of_dice in (7, 11):
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12):
    game_status = "LOST"
else:
    game_status = 'CONTINUE'
    target = sum_of_dice
    print(f'{player_name} your next target is : {target}')

while game_status == 'CONTINUE':
    input("enter to continue ...")
    die_value = roll_dice()
    display_dice(die_value)
    sum_of_dice = sum(die_value)

    if sum_of_dice == target:
        game_status = 'WON'
    elif sum_of_dice == 7:
        game_status = 'LOST'


if game_status == 'WON':
    print(f'{player_name}, you won!!!')
else:
    print(f'{player_name}, you lose!!!')
