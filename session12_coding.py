###Session 12 Coding

##Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##Open raw data
raw_data=pd.read_csv("hotelbookingdata.csv")
df = raw_data.assign(nnights=1) #Adding a new column with default value 1
del raw_data #Deleting raw data to save memory

##Cleaning
df['acc_type'] = df["accommodationtype"].str.split("@").str[1].str.strip() #Extract accommodation type
df['acc_type'].value_counts() #Count occurrences of each accommodation type

df['guestreviewsrating'].value_counts(dropna=False) #Count occurrences of each guest review rating and include NaN values
df['ratings'] = df['guestreviewsrating'].str.split('/').str[0].str.strip() #Extract the rating value before the '/' character
df['ratings'] = df['ratings'].astype(float) #Convert ratings to float data type
df['ratings'].dtypes #Check data type of guest review rating column which is object
df['ratings'].value_counts()

##Renaming variables
df = df.rename(columns = {'rating_reviewcount':'rating_count',
                          'rating2_ta':'ratingta',})
df.filter(regex = 'rating') #Select columns with 'rating' in their names

##Filtering variables
df.shape
#df['acc_type'].loc[df['acc_type'] == 'Hotel'].value_counts() #Filter rows where accommodation type is 'Hotel'
df.loc[df['acc_type'] == 'Hotel']
print(df['ratings'].isnull().sum()) #Count number of missing values in ratings column

df = df.loc[df['ratings'].notnull()] #Remove rows with missing ratings
#df = df.loc[~df['ratings'].isnull()] #same output as above
df = df.dropna(subset=['ratings']) #Another way to remove rows with missing ratings
df.shape

##Correcting wrongly documented observations
df['starrating'] = np.where(df['starrating'] == 0, None, df['starrating']) #Replace starrating values less than or equal to 0 with NaN
df['starrating'].value_counts(dropna=False)

#Removing duplicates
df.duplicated().sum() #Count number of duplicate rows
df = df.drop_duplicates() #Remove duplicate rows
df.shape

important_variables = [
    's_city',
    'hotel_id',
    'addresscountryname',
    'year',
    'month'
]
df = df.drop_duplicates(subset=important_variables) #Remove duplicates based on important variables
df.shape

#Descriptive statistics (lecture07 - data exploration on GitHub)
df.describe() #Get summary statistics for numerical columns

#Saving output
df.to_csv('output\hotelbookingdata_clean.csv', index=False) #Save cleaned DataFrame to a new CSV file