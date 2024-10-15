import json
import math
import statistics
from types import NoneType

import numpy as np
from fontTools.merge.util import sumLists

from lab4aa import average

# Open and read the JSON file
with open('datasets\counties.json', 'r') as file:
    data = json.load(file)

# Print the data
print(data[0]['bls']['2008']['employed'])
#print(data)
# (print(type(data[0]['deaths']['homicides'])))
# print(type(3))
# sumlist = data[0]['age']
# print(sumlist)
# print(statistics.variance(sumlist))
#sumLists=[data[0][]]
#sumlist=[data[0]['noaa']['temp-jan'], data[0]['noaa']['temp-apr'], data[0]['noaa']['temp-jul'], data[0]['noaa']['temp-oct']]
#print(sum(sumlist))
# for i in data['covid-deaths']:
#for i in data:
 #   var_data = (i['noaa']['temp-jan'], i['noaa']['temp-apr'], i['noaa']['temp-jul'], i['noaa']['temp-oct'])
  #  print(i['population']['2010'])
    #av_temp = (i['noaa']['temp-jan']+i['noaa']['temp-apr']+i['noaa']['temp-jul']+i['noaa']['temp-oct'])
    #diff = abs(av_temp - i['noaa']['temp-jan']) + ...
#    print(i['name'])
#    print(i['state'])
#    print(i['noaa']['temp'])
    #print(sum(i['noaa']['temp-jan'], i['noaa']['temp-apr'], i['noaa']['temp-jul'], i['noaa']['temp-oct']))

def least_var(data: data):
    county = data[0]['name']
    state = data[0]['state']
    var = 100000
    for i in data:
        var_data=(i['noaa']['temp-jan'], i['noaa']['temp-apr'], i['noaa']['temp-jul'], i['noaa']['temp-oct'])
        small_var = statistics.variance(var_data)
        if small_var < var:
            var=small_var
            county=i['name']
            state=i['state']
    return county, state, var #????????

# print(least_var(data))
# generated_sentence_variance= '{county} , {state} is the {description} county'
# county=least_var(data)[0]
# state=least_var(data)[1]
# description='least temperature variant'
# print(generated_sentence_variance.format(county, state, description))

generated_sentence_variance = '{county}, {state} is the {description} county'
county = least_var(data)[0]
state = least_var(data)[1]
description = 'least temperature variant'
temp_variance_sentence = generated_sentence_variance.format(county=county, state=state, description=description)
print(temp_variance_sentence)


def greatest_var(data: data):
    county = data[0]['name']
    state = data[0]['state']
    var = 1
    for i in data:
        var_data=(i['noaa']['temp-jan'], i['noaa']['temp-apr'], i['noaa']['temp-jul'], i['noaa']['temp-oct'])
        large_var = statistics.variance(var_data)
        if large_var > var:
            var=large_var
            county=i['name']
            state=i['state']
    return county, state, var #????????
greatest_var(data)
print(greatest_var(data))

def increase(data: data):
    county = data[0]['name']
    state = data[0]['state']
    slope = 0
    for i in data:
        x= [1,2,3,4,5,6,7,8,9,10]
        y= [i['population']['2010'], i['population']['2011'], i['population']['2012'], i['population']['2013'], i['population']['2014'], i['population']['2015'], i['population']['2016'], i['population']['2017'], i['population']['2018'], i['population']['2019'] ]
        slope_new= statistics.linear_regression(x,y)[0]
        if slope_new>slope:
            slope=slope_new
            county = i['name']
            state = i['state']
    return county, state, slope

print(increase(data))

def decrease(data: data):
    county = data[0]['name']
    state = data[0]['state']
    slope = 1000000000
    for i in data:
        x= [1,2,3,4,5,6,7,8,9,10]
        y= [i['population']['2010'], i['population']['2011'], i['population']['2012'], i['population']['2013'], i['population']['2014'], i['population']['2015'], i['population']['2016'], i['population']['2017'], i['population']['2018'], i['population']['2019'] ]
        slope_new= statistics.linear_regression(x,y)[0]
        if slope_new<slope:
            slope=slope_new
            county = i['name']
            state = i['state']
    return county, state, slope

print(decrease(data))

def most_deaths(data: data):
    county = data[0]['name']
    state = data[0]['state']
    death = 0
    for i in data:
        if i['deaths']['suicides'] is None:
            suicides=0
        else:
            suicides=i['deaths']['suicides']
        if i['deaths']['firearm suicides'] is None:
            firearm_suicides=0
        else:
            firearm_suicides=i['deaths']['firearm suicides']
        if i['deaths']['homicides'] is None:
            homicides=0
        else:
            homicides=i['deaths']['homicides']
        if i['deaths']['vehicle'] is None:
            vehicle=0
        else:
            vehicle=i['deaths']['vehicle']

        deaths_new= suicides + firearm_suicides + homicides + vehicle
        if deaths_new>death:
            death = deaths_new
            county = i['name']
            state = i['state']
    return county, state, death
#
print(most_deaths(data))

def most_educated(data:data):
    county = data[0]['name']
    state = data[0]['state']
    educated = 0
    for i in data:
        new_educated= i['edu']['bachelors+']
        if new_educated>educated:
            educated=new_educated
            county = i['name']
            state = i['state']
    return county, state, educated

print(most_educated(data))

def least_educated(data:data):
    county = data[0]['name']
    state = data[0]['state']
    educated = 100
    for i in data:
        new_educated= i['edu']['bachelors+']
        if new_educated<educated:
            educated=new_educated
            county = i['name']
            state = i['state']
    return county, state, educated
print(least_educated(data))




def female_skew(data:data):
    county = data[0]['name']
    state = data[0]['state']
    female = 0
    for i in data:
        new_female=i['female']/(i['female']+i['male'])
        if new_female>female:
            female = new_female
            county = i['name']
            state = i['state']
    return county, state, female

print(female_skew(data))

def male_skew(data:data):
    county = data[0]['name']
    state = data[0]['state']
    female = 100
    for i in data:
        new_female=i['female']/(i['female']+i['male'])
        if new_female<female:
            female = new_female
            county = i['name']
            state = i['state']
    return county, state, 1-female

print(male_skew(data))

def oldest(data:data):
    county = data[0]['name']
    state = data[0]['state']
    old = 0
    for i in data:
        new_oldest=i['age']['65-69']+i['age']['70-74']+i['age']['75-79']+i['age']['80-84']+i['age']['85+']
        if new_oldest>old:
            old=new_oldest
            county = i['name']
            state = i['state']
    return county, state, old
print(oldest(data))

def youngest(data:data):
    county = data[0]['name']
    state = data[0]['state']
    old = 100
    for i in data:
        new_oldest=i['age']['65-69']+i['age']['70-74']+i['age']['75-79']+i['age']['80-84']+i['age']['85+']
        if new_oldest<old:
            old=new_oldest
            county = i['name']
            state = i['state']
    return county, state, 1-old
print(youngest(data))

def least_age_var(data: data):
    county = data[0]['name']
    state = data[0]['state']
    var = 100000
    for i in data:
        var_data=(i['age']['0-4'], i['age']['5-9'], i['age']['10-14'], i['age']['15-19'], i['age']['20-24'], i['age']['25-29'], i['age']['30-34'], i['age']['35-39'], i['age']['40-44'], i['age']['45-49'], i['age']['50-54'], i['age']['55-59'], i['age']['60-64'], i['age']['65-69'], i['age']['70-74'], i['age']['75-79'], i['age']['80-84'], i['age']['85+'])
        small_var = statistics.variance(var_data)
        if small_var < var:
            var=small_var
            county=i['name']
            state=i['state']
    return county, state, var

print(least_age_var(data))

# def employment(data:data):
#     county = data[0]['name']
#     state = data[0]['state']
#     for i in data:
#         if i['bls'] is None:
#             return i

def employment(data: list[dict]) -> list[dict]:
    """Function to find counties without the BLS section."""
    missing_bls = []  # List to collect items without the BLS section

    for i in data:
        if 'bls' not in i:
            missing_bls.append(i['name'])

    return missing_bls


print(employment(data))

def highest_employment(data:data):
     county = data[0]['name']
     state = data[0]['state']
     employment=0
     for i in data:
         #print(i.keys())
            if 'bls' in i:
                employment_data= [i['bls']['2004']['employed']+i['bls']['2008']['employed']+i['bls']['2012']['employed']+i['bls']['2016']['employed']+i['bls']['2020']['employed']]
                employment_new=average(employment_data )
                if employment_new>employment:
                    employment=employment_new
                    county = i['name']
                    state = i['state']
     return county, state, employment
print(highest_employment(data))


def lowest_employment(data: data):
    county = data[0]['name']
    state = data[0]['state']
    employment = math.inf
    for i in data:
        # print(i.keys())
        if 'bls' in i:
            employment_data = [
                i['bls']['2004']['employed'] + i['bls']['2008']['employed'] + i['bls']['2012']['employed'] +
                i['bls']['2016']['employed'] + i['bls']['2020']['employed']]
            employment_new = average(employment_data)
            if employment_new < employment:
                employment = employment_new
                county = i['name']
                state = i['state']
    return county, state, employment


print(lowest_employment(data))

with open('report.md', 'w')as mdfile:
    mdfile.write('#Lab6:data\n')
    mdfile.write('Hawaii County HI is the Least Variance for Temperature\n')
    mdfile.write('yukon-kyukuk census area AK is the Greatest Variance for Temperature\n')
    mdfile.write('maricopa county is the fastest growing population\n')
    mdfile.write(temp_variance_sentence + '\n')









