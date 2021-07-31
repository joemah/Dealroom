import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict


def chech_for_nan(data):
   
    isnan = data.isnull().sum().any()
    if isnan == True:
        print("There are NaN values in the dataset\n\nCheck Indvidual columns:\n")
    #print(data.isnull().all())
    for col in data.columns:
        if data[col].isnull().all() is True:
            print(f'Column "{col}" is empty')
        elif data[col].isnull().any():
            print(f'The column "{col}" has some NaN values')
        else:
            print(f'The column "{col}" is good')
            


def check_for_duplicates(data):

    isdup = data.duplicated().sum().any()
    if isdup == True:
        print("There are duplicate rows in the dataset\n\nCheck Indvidual columns:\n")
    for col in data.columns:
        if data[col].duplicated().any():
            print(f'Column "{col}" has some duplicates')
        else:
            print(f"The column '{col}' doesn't have duplicates")


def get_duplicates_indexes(data,col):

   
    if (len(list(data[col])) != len(set(list(data[col])))) is False:
        return 'There are no duplicates'

    else:
        duplicates = set([j for j in list(data[col]) if list(data[col]).count(j)>1])
        counts = [list(data[col]).count(j) for j in duplicates]
        rows = []
        for d in duplicates:
            row = [num for num, k in enumerate(list(data[col])) if k == d]
            rows.append(row)
        staff = ['value_counts', 'rows']
        #print(staff)
        dupl_elements = dict(zip(staff,[(duplicates, counts), rows]))
        
        return dupl_elements
        
        
def get_all(data):
    
    duplit = defaultdict(list)
    
    
    for i in range(data.shape[1]):
        duplit[data.columns[i]].append(get_duplicates_indexes(data,data.columns[i]))
        
    return dict(duplit)
