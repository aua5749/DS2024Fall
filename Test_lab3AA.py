"""Module implementing functions for testing the functions in lab 2 and 3
completed by Augustin Au on 2024-09-17 fo DS-1043"""


from lab2AA import time_elapsed, is_even, is_odd, area, perimeter, volume, surface_area, get_square_color, prettify_time, right_justify, center_justify
from lab3aa import fizz_buzz, ordinal_suffix
import time


def test_time_elapsed():
    """Function is used to test the time_elapsed function"""
    assert time_elapsed(round(time.time())-1) ==(0,0,0,1)
    assert time_elapsed(round(time.time())-2) ==(0,0,0,2)
print(test_time_elapsed())


def test_is_even():
    """Function is used to test the is_even function"""
    assert is_even(4.0) is True
    assert is_even(5.0) is False
    assert is_even(5.5) is False
    assert is_even(-1) is False

print(test_is_even())

def test_is_odd():
    """Function is used to test the is_odd function"""
    assert is_odd(5) is True
    assert is_odd(4) is False
    assert is_odd(5.5) is False
    assert is_odd(-3) is True #????

print(test_is_odd())


def test_area():
    """Function is used to test the area function"""
    assert area(2,2) ==4
    assert area(-3,2) ==-6
    assert area(-3, -3) ==9
print(test_area())

def test_perimeter():
    """Function is used to test the perimeter function"""
    assert perimeter(1,2) ==6
    assert perimeter(-1,-1) ==-4
    assert perimeter(-3,1) ==-4
print(test_perimeter())

def test_volume():
    """Function is used to test the volume function"""
    assert volume(1,2,3) ==6
    assert volume(-1,2,-3) ==6
    assert volume(-1,2,3) ==-6
print(test_volume())

def test_surface_area():
    """Function is used to test the surface_area function"""
    assert surface_area(1,2,3) ==22
    assert surface_area(-1,2,3) ==2
print(test_surface_area())


def test_get_square_color():
    """Function is used to test the get_square_color function"""
    assert get_square_color(1,1) == 'white'
    assert get_square_color(1,2) == 'black'
    assert get_square_color(-1,5) == 'N/A'
    assert get_square_color(2,10) =='N/A'
print(test_get_square_color())


def test_prettify_time():
    """Function is used to test the prettify_time function"""
    assert prettify_time (1,1,1,1) == '1 days, 1 hours, 1 minutes, 1 seconds'
    assert prettify_time (2,0,0,2) == '2 days, 2 seconds'
    assert prettify_time (0,5,0,0) == '5 hours, '
print(test_prettify_time())

#print(right_justify('hi', 5))
def test_right_justify():
    """Function is used to test the right_justify function"""
    assert right_justify ('hi', 10) == '        hi'
    assert right_justify ('abcd', 2) == 'N/A'
    assert right_justify ('abcd', -5) == 'N/A'
print (test_right_justify())


def test_center_justify():
    """Function is used to test the center_justify function"""
    assert center_justify ( 'abcd', 10) == '   abcd'
    assert center_justify ( 'abcd', 7) == '  abcd'
    assert center_justify ('abcd', -10) == 'N/A'
    assert center_justify('abcd', 3) == 'N/A'
print (test_center_justify())


def test_fizz_buzz():
    """Function is used to test the fizz_buzz function"""
    assert fizz_buzz(6) =='1,2,Fizz,4,Buzz,Fizz,'
    assert fizz_buzz(15) =='1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,Fizzbuzz,'
print(test_fizz_buzz())

def test_ordinal_suffix():
    """Function is used to test the ordinal_suffix function"""
    assert ordinal_suffix(22) =='22nd'
    assert ordinal_suffix(31) =='31st'
    assert ordinal_suffix(53) ==('53rd')
print(test_ordinal_suffix())



