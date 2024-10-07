"""Module implementing functions for fizzbuzz and ordinal suffix
completed by Augustin Au on 2024-09-17 fo DS-1043"""

def fizz_buzz (up_to: int) ->str:
    """This function is meant to return Fizz when it is a multiple of 3, Buzz when it is a multiple of 5, Fizzbuzz when it is a multiple of both 3 and 5, and the integer if it is neither. The function should go from 1 to the specified integer."""
    statement = ''
    for x in range(1,up_to +1):
        if x % 3 ==0 and x % 5 == 0:
            statement = statement + 'Fizzbuzz,'
        elif x % 3 ==0:
            statement = statement + 'Fizz,'
        elif x % 5 == 0:
            statement = statement + 'Buzz,'
        else:
            statement =statement + str(x) +','
    return statement
#print(fizz_buzz(5))


def ordinal_suffix (number: int) ->str:
    """The function should return the given number and its appropriate suffix"""
    remainder = number%10
    if remainder ==1:
        return str(number) + 'st'
    elif remainder ==2:
        return str(number) + 'nd'
    elif remainder ==3:
        return str(number) + 'rd'
    else:
        return str(number) + 'th'

#print(ordinal_suffix(91))




