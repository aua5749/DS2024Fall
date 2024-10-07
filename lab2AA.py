"""Module implementing functions for Odd and Even, Time, Space, Boardsquare color, Pretty Print, and Justification
completed by Augustin Au on 2024-09-04 fo DS-1043"""

import time


Number = int|float

def is_odd(number: float) -> bool:
    """Function determines whether the input is odd or not."""
    return number%2 ==1

#print(is_odd(-3))
#print(-3%2)
# below is better way
Number = int|float

def is_oddbetter(x: Number) -> bool:
    return x%2 ==1



def is_even(number: float) -> bool:
    """Function determines whether the input is odd or not."""
    return number%2 ==0


#print(is_even(5))
#print(is_even(8))

#time

def time_elapsed (timestamp: int) -> tuple[int, int, int, int]:
    """ Function returns a tuple that contains the days, hours, minutes, and seconds between the time the function is called and the time represented by timestamp"""
    curr= time.time()
    elpTime = round(curr-timestamp)
    day = elpTime//(60*60*24)
    DayRemainder=elpTime%(60*60*24)
    hour = DayRemainder//(3600)
    HourRemainder= DayRemainder%(3600)
    minutes = HourRemainder//60
    MinuteRemainder = HourRemainder%60
    seconds=(MinuteRemainder)
    return (day,hour, minutes, seconds)

#print(time_elapsed(round(time.time())-2))



#space
def area(length: float, width: float) -> float:
    """Function returns the area when given the length and width."""
    Area = length*width
    return(Area)
#print(area(2,3))
def perimeter (length: float, width: float) -> float:
    """Function returns the perimeter when given the length and width."""
    Perimeter = length + width +length +width
    return(Perimeter)
#print(perimeter(2,3))
def volume (length: float, width: float, height: float) -> float:
    """Function returns the volume when given the length, width, and height."""
    Volume = length*width*height
    return(Volume)
#print(volume(2,3,4))
def surface_area(length: float, width: float, height: float) -> float:
    """Function returns the surface area when given the length, width, and height."""
    Surfacearea = (length*width*2)+(length*height*2)+(width*height*2)
    return(Surfacearea)
#print(surface_area(-1,2,3))

#board square color
def get_square_color(column:int, row:int) -> str:
    """Function tells whether a square from a 7x7 board is black or white."""
    if column|row > 7:
        return('N/A')
    if column|row <=0:
        return('N/A')
    if column-row ==0:
        return('white')
    elif is_even(abs(column-row)) == True:
        return('white')
    else:
        return('black')

#print(get_square_color(-1,5))

#pretty print
def prettify_time(days: int, hours: int, minutes: int, seconds: int) -> str:
    """The function returns a string that prints the days, hours, minutes, and seconds when given 4 integers."""
    if days !=0:
        part1 =  str(days) +' days, '
    else:
        part1 = ''
    if hours !=0:
        part2 = str(hours) + ' hours, '
    else:
        part2 = ''
    if minutes !=0:
        part3 = str(minutes) + ' minutes, '
    else:
        part3 = ''
    if seconds !=0:
        part4 = str(seconds) + ' seconds'
    else:
        part4 = ''
    return part1 + part2 + part3 + part4
#print(prettify_time(3, 0, 2, 3))

#alternative way
#def prettify_time(days: int, hours: int, minutes: int, seconds: int) -> str:
 #   values= (days, hours, minutes, seconds)
  #  labels = ('day', 'hour', 'minute', 'second')
   # filter(lambda t: t[0] == 0, zip(values, labels))



#justification
def right_justify(content: str, width: int) ->str:
    """Function right justifys the given string relative to a given column width."""
    spacing = width-len(content)
    if width <=0|len(content):
        return 'N/A'
    else:
        return ' '*spacing +content
#print(right_justify('abcd', 8))

def center_justify(content: str, width: int) ->str:
    """Function center justifys the given string relative to a given column width"""
    spacing = round((width - len(content)) / 2)
    if width <= len(content):
        return 'N/A'
    else:
        return ' '*spacing +content
#print(center_justify('abcd', 5))










