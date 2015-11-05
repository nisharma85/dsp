#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
import os
os.getcwd()
os.chdir('C:/Users/shani16/Documents/Python_dsp')

import csv


def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data


# ---- run code ---- #

data = "football.csv"
f  =read_data(data)        
   # COMPLETE THIS FUNCTION

def get_min_score_difference(self, parsed_data):
    parsed_data.pop(0) #removes headers which are ['Team', 'Games', 'Wins'...
    goals = [x[5] for x in parsed_data] #the x here is each "line" and you are telling it to make goals the 5 element in each line x
    goals_allowed = [x[6]for x in parsed_data] #see above
    values = [float(x) - float(y) for x, y in zip(goals, goals_allowed)] 
    return values.index(min(values))
      
      
    # COMPLETE THIS FUNCTION

def get_team(self, index_value, parsed_data):
    print parsed_data[0]
    teams = [x[0] for x in parsed_data]
    return teams[index_value]
    
import pandas as pd


def smallest_gap(fname, col1, col2, result_col):
    data = pd.read_csv(fname)
    diff = data[col1] - data[col2]
    smallest = data[diff == diff.min()]
    return smallest[result_col].values[0]
