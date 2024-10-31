

import os
import string
from distutils.dep_util import newer

from matplotlib.table import table

from numba.cpython.unicode import join_list
from numba.typed.listobject import new_list
from numpy.ma.core import append
from scipy.interpolate.dfitpack import types
from lab2AA import right_justify
from lab2AA import center_justify

lista=(1,2,3,4)
listb=[(4,5,6,7), (1,2,3,4), (3,4,5,6.3729,)]
listc=(1,2,3,4)
listd=(1,2,3,4)
ls = [['name','place'],[56,8],[['job'],['occupation']],['c']]
# #def create_table(header, data):
#     s = []
#     for i in header:
#         s.append('|' + str(i) + '...')
#         a = []
#         for x in data:
#             a.append('|' + str(x)+ '...''\n')
#     return s,a
#
# ls1,ls2= create_table(lista, listb)
# print(ls1)
# print(ls2)
#
print(len(listb[0]))
def create_table(header, list_of_list: list):
    header_row_max_len = []
    for columns in range(len(header)):
        header_row_max_len.append(len(str(header[columns])))
    data_max_len = []
    for column in range(len(list_of_list[0])):
        data_column_len_prelim = []
        for row in list_of_list:
            data_column_len_prelim.append(len(str(row[column])))
        data_max_len_prelim2 = max(data_column_len_prelim)
        data_max_len.append(data_max_len_prelim2)

    for d in range(len(header_row_max_len)):
        if data_max_len[d]> header_row_max_len[d]:
            header_row_max_len[d]= data_max_len[d]
        else:
            header_row_max_len[d]=header_row_max_len[d]
    top_row=''

    for i in header:
        i=round(i,2)
        n=0
        top_row += '|'+str(right_justify(str(i),header_row_max_len[0+n]))
        n=n+1
    table_content=''
    for x in list_of_list:
        subsequent_row='\n'
        if len(header) !=len(x):
            raise Exception("length of header is not equal to length of data row")
        for y in x:
            #if len(header) != len()
            data_type= type(y)
            if y is None:
                y=''
            y=round(y,2)
            n=0
            subsequent_row+= '|' + str(right_justify(str(y), header_row_max_len[0+n]))
            n=n+1
        table_content+=subsequent_row

    table_answer= top_row + table_content

    return table_answer
print(create_table(lista, listb))
import shutil
# def view_table(header, data, max_width=(shutil.get_terminal_size()).columns, file=report_lab7.md):
#     print (create_table(header, data))
    # this function should call `create_table`
    # pass the file keyword parameter to the print function
    # this will allow writing to a stream for testing



def merge_sorted_list(*lists):
    big_list = []
    for i in lists:
        big_list+=i
    new_sorted_list = []
    while len(big_list)>0:
        new_sorted_list.append(min(big_list))
        big_list.remove(min(big_list))
    return new_sorted_list





help(join_list)

sample='Hello World'
print(len(sample))
print(sample[0])
print(chr(66))
print(ord('a'))
def ceasar(string_sample, shift):
    new_string=''
    for i in range(len(string_sample)):
        character=string_sample[i]
        if character in string.ascii_uppercase:
            number=ord(character)
            new_character=chr(((number-65)+shift)%26+65)
            new_string+=new_character
        elif character in string.ascii_lowercase:
            number=ord(character)
            new_character=chr(((number-97)+shift)%26+65)
            new_string+=new_character
        else:
            new_character=character
            new_string+=new_character
    return new_string

print(ceasar('Hello World',1))








