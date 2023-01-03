# import math
# 'Enter student name'
# 'enter python score'
# 'enter app inventor score'
# 'enter scratch score'
# "matin's avergae is 19.6"
# name = ''
# ave = 19.999999
# print(math.ceil(ave))
# print(math.floor(ave))
# print(round(ave))
# print(f"{name}'s average is {ave:.1f}")
'''
Exercise:
برنامه ای بنویسید که هزینه بنزیم مصرفی از تهران تا مشهد را محاسبه نماید
(مسیر رفت و برگشت)

ورودی برنامه میزان مصرف خودرو میباشد
بعنی در هر صد کیلومتر چند لیتر؟

مسافت تهران تا مشهد هزار کیلومتر می باشد

خروجی برنامه : هزینه بنزین مصرفی برای رفت و برگشت

تا 60 لیتر ، بنزین با نرخ 1500 محاسبه می شود
برای بالاتر از 60 لیتر قیمت بنزین بازای هر لیتر 3000 تومان می باشد.


'''


# print(max([1, 2, 30]))
# print(min([11, 2, 30]))
# print(abs(-1))
# print(sum([1,2,3,4,5]))

# def square(x):
#     return x**2


# output = square(2)
# print(output)

# def max_value(num1, num2, num3):
#     max_value = num1
#     if num2 > max_value:
#         max_value = num2
#     if num3 > max_value:
#         max_value = num3

#     return max_value


# output = max_value(10, 9, 90)
# print(output)

import random
frequency_1, frequency_2, frequency_3, frequency_4, frequency_5, frequency_6 = (
    0, 0, 0, 0, 0, 0)
for i in range(10_000_000):
    die = random.randint(1, 6)
    if die == 1:
        frequency_1 += 1
    elif die == 2:
        frequency_2 += 1
    elif die == 3:
        frequency_3 += 1
    elif die == 4:
        frequency_4 += 1
    elif die == 5:
        frequency_5 += 1
    elif die == 6:
        frequency_6 += 1
print(f'Face{"Frequency":>14}')
print(f'{1:>4}{frequency_1:>14}')
print(f'{2:>4}{frequency_2:>14}')
print(f'{3:>4}{frequency_3:>14}')
print(f'{4:>4}{frequency_4:>14}')
print(f'{5:>4}{frequency_5:>14}')
print(f'{6:>4}{frequency_6:>14}')
