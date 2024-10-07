"""Module implementing functions for testing the functions in lab 4
completed by Augustin Au on 2024-09-17 fo DS-1043"""

import random
from lab4aa import min, max, my_sum, average, median, mode, roll_dice


listA = [1,3,5,7,8,4]
listB = [-3,6,8,2,-6]
def test_min():
    """Function is used to test the min function"""
    assert min(listA) ==1
    assert min (listB) ==-6
print(test_min())

def test_max():
    """Function is used to test the max function"""
    assert max(listA) ==8
    assert max(listB) ==8
print(test_max())

def test_my_sum():
    """Function is used to test the my_sum function"""
    assert my_sum(listA) == 28
    assert my_sum(listB) == 7
print(test_my_sum())

def test_average():
    """Function is used to test the average function"""
    assert average(listA) == 4+2/3
    assert average(listB) == 7/5
print(test_average())


listA = [1,3,5,7,8,4]
listB = [-3,6,8,2,-6]
def test_median():
    """Function is used to test the median function"""
    assert median(listA) ==4.5
    assert median(listB) ==2
print(test_median())

listc = [1,2,5,5,5,3,7]
def test_mode():
    """Function is used to test the mode function"""
    assert mode(listc) ==5
print(test_mode())

def test_dice():
    """Function is used to test the test_dice function"""
    assert len(roll_dice(2,6)) ==2
    x,y = roll_dice(2,6)
    assert x>0 and x <=6
    assert y>0 and y<=6
print(test_dice())




