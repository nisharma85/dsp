#Import modules
import csv
import pandas as pd
import numpy as np
from string import replace
import os

#Change directory 
os.getcwd()
os.chdir('C:/Users/shani16/Documents/Python_dsp')

################################################################
#Part 1:

#Bring in data
data=pd.read_csv('faculty.csv') #bring in data file
data[:3] #Look at first three rows
data = data.rename(columns=lambda x: x.strip()) #remove spaces in column names
data.columns #look at column names


#Find unique degrees
degree= pd.melt(pd.DataFrame(list(data.degree.str.split()))) #Extract degrees by space and melt all degrees in one column
degree['value'] = degree.value.apply(lambda x: str(x).strip()) #Remove white space
degree['value'] = degree['value'].str.replace('.', '')#Remove "." within degree column
degree =  degree[(degree['value'] !="None")] #Select only values that are not "None"
degree =  degree[(degree['value'] !="0")] #Select only values that are not "0"
g = degree['value'].value_counts() #Create a "variable" with the different degrees and their counts

 print('We have a total of %.0f degrees and the following are the lists and frequencies: ' % g.count()) 
 print (g)
 
##########################

data['title1'] = data['title'].apply(lambda x: x.split(' ')[0]) #extract the first word in title
data['title2']= [x + " "+ "Professor" if x!="Professor" else x for x in data.title1]
title_count=data['title2'].value_counts() #get counts by title type

 print('We have a total of %.0f titles and the following are the lists and frequencies: ' % title_count.count()) 
 print (title_count)

email=[] #Create empty list 
email.append(data.email) #Append the email columns into the empty list email

 print('The following are the lists of emails: ')
 print email


##########################



data['name_email'], data['domain'] = zip(*data['email'].apply(lambda x: x.split('@', 1))) #Split out domain from email address and create new variable called "domain"
email1=data['domain'].value_counts()


 print('We have a total of %.0f unique domains  and the following are the lists and frequencies: ' % email1.count()) 
 print email1
