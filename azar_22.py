
# star = int(input('enter how many star numbers you want> '))
# for i in range(star):
#     print((i+1) * '*')

# for i in range(star, 0, -1):
#     print(i * '*')

# lines = int(input('enter how many lines numbers you want> '))
# z = lines - 1
# x = 1
# for i in range(lines):
#     print(' '*z + x * '*' + ' '*z)
#     z -= 1
#     x += 2

# for i in range(lines//2):
#     print(' ' * (lines - 1) + '*' + ' ' * (lines - 1))


# exercise:
'''
write a loop to do like this:
Enter string 1/5: the blue moon
Enter string 2/5: the red guitar
Enter string 3/5: go home
Enter string 4/5: spill the beans
Enter string 5/5: winter in Oklahoma
'''
string_list = []
for i in range(1, 6):
    string = input(f'enter string {i}/5: ')
    string_list.append(string)


'''
write another loop to show entered strings reverse like this:

String 5/5: winter in Oklahoma
String 4/5: spill the beans
String 3/5: go home
String 2/5: the red guitar
String 1/5: the blue moon
'''
for i in range(4, -1, -1):
    print(f'string {i+1}/5', string_list[i])
