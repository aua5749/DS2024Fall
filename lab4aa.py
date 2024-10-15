"""Module implementing functions for min, max, my_sum, average, median, mode, and dice roll
completed by Augustin Au on 2024-09-17 fo DS-1043"""

import random
from logging import raiseExceptions

from lab2AA import is_odd, is_even

Sequence = list |tuple
Number = int | float
def min(numbers: Sequence) -> Number | None:
    "Function returns the smallest value in a sequence"
    order = sorted(numbers)
    if len(numbers) == 0:
        return None
    else:
        return order[0]

def min_exception(numbers: Sequence) -> Number:
    "Function returns the smallest value in a sequence"
    order = sorted(numbers)
    if len(numbers) ==0:
        raise Exception("sequence is empty")
    return order[0]


listempty = ()
lista = (1,3,5,4,1,7,)
#min_exception(listempty)

def max(numbers: Sequence) -> Number | None:
    """Function returns the largest value in a sequence"""
    order = sorted(numbers, reverse=True)
    if len(numbers) == 0:
        return None
    else:
        return order[0]

def max_exception(numbers: Sequence) -> Number | None:
    """Function returns the largest value in a sequence"""
    order = sorted(numbers, reverse=True)
    if len(numbers) == 0:
        raise Exception("sequence is empty")
    return order[0]

def my_sum (numbers: Sequence) -> Number | None:
    """Function returns the sum of a sequence"""
    sum = 0
    if len(numbers) ==0:
        return None
    else:
        for x in numbers:
            sum = sum+x
        return sum
#print(sum(lista))

def my_sum_exception (numbers: Sequence) -> Number:
    """Function returns the sum of a sequence"""
    sum = 0
    if len(numbers) ==0:
        raise Exception("sequence is empty")
    else:
        for x in numbers:
            sum = sum+x
        return sum

#print(my_sum_exception(lista))


def average (numbers: Sequence) -> Number | None:
    """Function returns the average of a sequence"""
    if len(numbers) ==0:
        return None
    else:
        prelim_sum = my_sum(numbers)
        avg = prelim_sum/len(numbers)
        return(avg)
#print(average(lista))

def average_exception (numbers: Sequence) -> Number | None:
    """Function returns the average of a sequence"""
    if len(numbers) ==0:
        raise Exception ("sequence is empty")
    else:
        prelim_sum = my_sum(numbers)
        avg = prelim_sum/len(numbers)
        return(avg)

def median (numbers: Sequence) -> Number | None:
    """Function returns the median of a sequence"""
    ascending = sorted(numbers)
    print(ascending)
    print(type(ascending), type(numbers))
    if len(ascending) ==0:
        return None
    elif is_odd(len(ascending)) is True:
        return ascending[(((len(ascending))//2))]
    else:
        pseudo_mid = len(ascending) // 2
        return ((ascending[pseudo_mid-1]+ascending[pseudo_mid]))/2

def median_exception (numbers: Sequence) -> Number | None:
    """Function returns the median of a sequence"""
    ascending = sorted(numbers)
    print(ascending)
    print(type(ascending), type(numbers))
    if len(ascending) ==0:
        raise Exception ("sequence is empty")
    elif is_odd(len(ascending)) is True:
        return ascending[(((len(ascending))//2))]
    else:
        pseudo_mid = len(ascending) // 2
        return ((ascending[pseudo_mid-1]+ascending[pseudo_mid]))/2



listB = [-3,6,8,2,-6]
print(median(lista))
#print(round((len(lista)/2)+0.5))

def mode (numbers: Sequence) ->  Number | None:
    """Function returns the mode of a sequence"""
    if len(numbers) ==0:
        return None
    counts = {}
    mode = numbers[0]
    for x in numbers:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x]= counts[x] +1
        if counts[x] > counts[mode]:
            mode = x
    return mode
#print(mode(lista))
def mode_exception (numbers: Sequence) ->  Number | None:
    """Function returns the mode of a sequence"""
    if len(numbers) ==0:
        raise Exception ("sequence is empty")
    counts = {}
    mode = numbers[0]
    for x in numbers:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x]= counts[x] +1
        if counts[x] > counts[mode]:
            mode = x
    return mode

#print(mode_exception(listempty))

def roll_dice (dice_numbers: int, face_number: int) -> tuple:
    """Function returns a tuple of dice roles based off of dice numbers and face numbers"""
    tuple_answer = ()
    for x in range(0,dice_numbers):
        number_generated = ((random.randint(1,face_number)),)
        tuple_answer = tuple_answer +number_generated
    return tuple_answer

def roll_dice_exception (dice_numbers: int, face_number: int) -> tuple:
    """Function returns a tuple of dice roles based off of dice numbers and face numbers"""
    tuple_answer = ()
    if dice_numbers==0 or face_number ==0:
        raise Exception("dice number or face number is zero")
    for x in range(0,dice_numbers):
        number_generated = ((random.randint(1,face_number)),)
        tuple_answer = tuple_answer +number_generated
    return tuple_answer

#print(roll_dice_exception(5,0))



random.seed()








