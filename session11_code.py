###Session 11. Data exploration and functions

print("Hello, Session 11!")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

ps = pd.Series(["a", 2, np.pi, 36]) # Create a Pandas Series with mixed data types
ps # Display the Series
type(ps) # Check the type of the object
print(ps.values) # Print the values of the Series
print(ps.index) # Print the index of the Series

print(ps[1:3]) # Slice the Series from index 1 to 2

##loc and iloc - label-based and integer-based indexing
#the difference is that loc uses the index labels while iloc uses the integer positions (such as 0, 1, 2,...)
ps1 = pd.Series(
    data=[
        "Introduction to Micro",
        "Game Theory",
        "Advanced Micro"
    ],
    index = [
        "Bachelor",
        "Master",
        "PhD"
    ]
)
ps1

ps1.loc["PhD"] # Access using label-based indexing and call corresponding value
ps1.loc[["Bachelor", "PhD"]] # Access multiple labels
ps1.iloc[[0,2]] # Access using integer-based indexing, gives same result as previous command
ps1.iloc[1:2] # Slice using integer-based indexing

dc_uni_graduation = {
    2022: 100,
    2023: 120,
    2024: 90
} # Create a dictionary
ps_uni_graduation = pd.Series(dc_uni_graduation) # Create a Series from a dictionary
ps_uni_graduation
print(ps_uni_graduation.index)
print(ps_uni_graduation.values)

dc_uni_enrollment = {
    2022: 150,
    2023: 80,
    2024: 120
}
ps_uni_enrollment = pd.Series(dc_uni_enrollment)
ps_uni_enrollment

df_uni = pd.concat([ps_uni_enrollment, ps_uni_graduation], axis=1) # Concatenate two Series into a DataFrame, axis = 1 means concatenate by columns
df_uni
df_uni_columns = ["Enrollment", "Graduation"] # Define column names
df_uni.columns = df_uni_columns # Assign column names to the DataFrame
df_uni

print(df_uni.iloc[-1,0]) # Access the last row and first column using iloc

df_uni.loc[[2023, 2024]]
ps1.loc["Bachelor":"PhD"] # Slice using label-based indexing

df_uni[(df_uni.Graduation >= 100) & (df_uni.Enrollment <100)] # Filter rows based on conditions

df_uni.reset_index(drop=False, inplace=True) # Reset index and keep the old index as a column
df_uni.rename({"index":"Year"}, axis="columns", inplace=True) # Rename the index column to "Year"
df_uni
#type of ({"index":"Year"}) is dict
df_uni[df_uni.Year.isin([2022, 2024])] # Filter rows where Year is either 2022 or 2024
df_uni[~df_uni.Year.isin([2022, 2024])] # Filter rows where Year is not 2022 or 2024

df_uni2 = [] # Create an empty list to store DataFrames
df_uni2.append([2022, 150, 100]) # Append a row to the list
df_uni2.append([2023, 80, 120])
df_uni2.append([2024, 120, 90])
df_uni2 = pd.DataFrame(df_uni2, columns=["Year", "Enrollment", "Graduation"]) # Convert the list to a DataFrame with specified column names
df_uni2

df_uni2 = df_uni2[["Year", "Graduation", "Enrollment"]] # Reorder columns
df_uni2.info() # Display information about the DataFrame
df_uni2.shape
type(df_uni2.shape) # Check the type of the shape attribute - it's a tuple

#raw_data = pd.read_csv("hotelbookingdata.csv") # Read a CSV file into a DataFrame
raw_data.head() # Display the first few rows of the DataFrame

raw_data["nnights"] =  1 # Create a new column 'nnights' and set its value to 1 for all rows
df = raw_data.assign(nnights = 0) # Another way to create a new column using assign method
df.head() # Display the first few rows of the modified DataFrame

df[["accommodationtype", "price"]] # Select specific columns from the DataFrame
df.filter(["accommodationtype", "price"]) # Another way to select specific columns using filter method
df.filter(regex="rating") # Select columns that match the regex pattern "rating"

df["accommodationtype"].str.split("@") # Split the strings in the 'accommodationtype' column by "@" character
df["acc_type"] = df["accommodationtype"].str.split("@").str[1].str.strip() # Extract the second part after splitting and remove leading/trailing spaces
df['acc_type'].value_counts() # Count the occurrences of each unique value in the 'acc_type' column