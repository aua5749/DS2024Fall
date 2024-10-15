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
    "retunrs least temperature variant county"
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

generated_sentence_least_variance = '{county}, {state} is the {description} county'
county = least_var(data)[0]
state = least_var(data)[1]
description = 'least temperature variant'
temp_variance_sentence = generated_sentence_least_variance.format(county=county, state=state, description=description)
print(temp_variance_sentence)


def greatest_var(data: data):
    "returns greatest temperature variant county"
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
generated_sentence_greatest_variance = '{county}, {state} is the {description} county'
county = greatest_var(data)[0]
state = greatest_var(data)[1]
description = 'greatest temperature variant'
temp_variance_greatest_sentence = generated_sentence_greatest_variance.format(county=county, state=state, description=description)
print(temp_variance_greatest_sentence)

def increase(data: data):
    "Returns fastest increasing population county"
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

generated_sentence_fastest_growing = '{county}, {state} is the {description} county'
county = increase(data)[0]
state = increase(data)[1]
description = 'fastest growing'
growing_sentence = generated_sentence_fastest_growing.format(county=county, state=state, description=description)
print(growing_sentence)

print(increase(data))

def decrease(data: data):
    "returns fastest shrinking population county"
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

generated_sentence_fastest_shrinking = '{county}, {state} is the {description} county'
county = decrease(data)[0]
state = decrease(data)[1]
description = 'fastest shrinking'
shrinking_sentence = generated_sentence_fastest_shrinking.format(county=county, state=state, description=description)
print(shrinking_sentence)

def most_deaths(data: data):
    "returns county with most deaths"
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

generated_sentence_deaths = '{county}, {state} is the {description} county'
county = most_deaths(data)[0]
state = most_deaths(data)[1]
description = 'greatest dying'
death_sentence = generated_sentence_fastest_growing.format(county=county, state=state, description=description)
print(death_sentence)

def most_educated(data:data):
    "returns most educated coutny"
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

generated_sentence_most_educated = '{county}, {state} is the {description} county'
county = most_educated(data)[0]
state = most_educated(data)[1]
description = 'most educated'
most_educated_sentence = generated_sentence_most_educated.format(county=county, state=state, description=description)
print(most_educated_sentence)

def least_educated(data:data):
    "returns least educated county"
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

generated_sentence_least_educated = '{county}, {state} is the {description} county'
county = least_educated(data)[0]
state = least_educated(data)[1]
description = 'least educated'
least_educated_sentence = generated_sentence_least_educated.format(county=county, state=state, description=description)
print(least_educated_sentence)




def female_skew(data:data):
    "returns most female skewed county"
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

generated_sentence_female_skew = '{county}, {state} is the {description} county'
county = female_skew(data)[0]
state = female_skew(data)[1]
description = 'most female skewed'
most_female_skew_sentence = generated_sentence_female_skew.format(county=county, state=state, description=description)
print(most_female_skew_sentence)

def male_skew(data:data):
    "returns most male skewed county"
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

generated_sentence_male_skew = '{county}, {state} is the {description} county'
county = male_skew(data)[0]
state = male_skew(data)[1]
description = 'most male skewed'
most_male_skew_sentence = generated_sentence_male_skew.format(county=county, state=state, description=description)
print(most_male_skew_sentence)

def oldest(data:data):
    "returns oldest county"
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

generated_sentence_oldest = '{county}, {state} is the {description} county'
county = oldest(data)[0]
state = oldest(data)[1]
description = 'oldest'
oldest_sentence = generated_sentence_oldest.format(county=county, state=state, description=description)
print(oldest_sentence)

def youngest(data:data):
    "returns youngest county"
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

generated_sentence_youngest = '{county}, {state} is the {description} county'
county = youngest(data)[0]
state = youngest(data)[1]
description = 'youngest'
youngest_sentence = generated_sentence_youngest.format(county=county, state=state, description=description)
print(youngest_sentence)

def least_age_var(data: data):
    "returns least age variant county"
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

generated_least_age_var = '{county}, {state} is the {description} county'
county = least_age_var(data)[0]
state = least_age_var(data)[1]
description = 'least age variant'
least_age_var_sentence = generated_least_age_var.format(county=county, state=state, description=description)
print(least_age_var_sentence)

# def employment(data:data):
#     county = data[0]['name']
#     state = data[0]['state']
#     for i in data:
#         if i['bls'] is None:
#             return i

# def employment(data: list[dict]) -> list[dict]:
#     missing_bls = []  # List to collect items without the BLS section
#
#     for i in data:
#         if 'bls' not in i:
#             missing_bls.append(i['name'])
#
#     return missing_bls


# print(employment(data))

def highest_employment(data:data):
     "returns county with highest employment"
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

generated_sentence_highest_employment = '{county}, {state} is the {description} county'
county = highest_employment(data)[0]
state = highest_employment(data)[1]
description = 'highest employment'
highest_employment_sentence = generated_sentence_highest_employment.format(county=county, state=state, description=description)
print(highest_employment_sentence)


def lowest_employment(data: data):
    "returns county with lowest employment"
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

generated_sentence_lowest_employment = '{county}, {state} is the {description} county'
county = lowest_employment(data)[0]
state = lowest_employment(data)[1]
description = 'lowest employment'
lowest_employment_sentence = generated_sentence_lowest_employment.format(county=county, state=state, description=description)
print(lowest_employment_sentence)

with open('report.md', 'w')as mdfile:
    mdfile.write('#Lab6:data\n')
    mdfile.write(temp_variance_sentence + '\n')
    mdfile.write(temp_variance_greatest_sentence + '\n')
    mdfile.write(growing_sentence + '\n')
    mdfile.write(shrinking_sentence + '\n')
    mdfile.write(death_sentence + '\n')
    mdfile.write(most_educated_sentence + '\n')
    mdfile.write(least_educated_sentence + '\n')
    mdfile.write(most_female_skew_sentence + '\n')
    mdfile.write(most_male_skew_sentence + '\n')
    mdfile.write(oldest_sentence + '\n')
    mdfile.write(youngest_sentence + '\n')
    mdfile.write(least_age_var_sentence + '\n')
    mdfile.write(highest_employment_sentence + '\n')
    mdfile.write(lowest_employment_sentence + '\n')









