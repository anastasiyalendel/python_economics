###Creating plots
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


##Functional approach
x = range(0,10)
y = [i ** 2 for i in x] #y contains squares of x values

plt.subplot(1,2,1) #Create a subplot with 1 row, 2 columns, and set the first plot as active
plt.plot(x,y, 'r--') #Create a line plot of x vs y and set line style to red dashed
plt.title("x-squared") #Add title to the plot
plt.xlabel("x") #Add x-axis label
plt.ylabel("y") #Add y-axis label
plt.legend("x") #Add legend to the plot
plt.subplot(1,2,2) #Set the second plot as active
plt.plot(y,x, 'g*-') #Set the second plot as active and create a green star-marked line plot of y vs x
plt.title('square root of x') #Add title to the second plot
plt.show() #Display the plots


##Object-oriented approach
#x = range(0,10)
#y = [i ** 2 for i in x] #y contains squares of x values

#fig = plt.figure() #Create a figure object
#axes1 = fig.add_axes([0,0,1,1]) #Add axes to the figure with specified dimensions [left, bottom, width, height]
#axes2 = fig.add_axes([0.1, 0.4, 0.4, 0.3]) #Add another axes to the figure

#Main figure
#axes1.plot(x,y, 'r')
#axes1.set_xlabel("x") #Set x-axis label
#axes1.set_ylabel("y") #Set y-axis label
#axes1.set_title("Simple x-squared") #Set title of the plot

#Additional figure
#axes2.plot(y,x, 'g') #Plot y vs x on the second axes
#axes2.set_xlabel("y") #Set x-axis label for the second plot
#axes2.set_ylabel("x") #Set y-axis label for the second plot
#axes2.set_title("Square root of x") #Set title for the second plot


##Read a file and do graph
df = pd.read_csv("ready_sp500_45_cos.csv") #Read data from CSV file
df.head() #Display first few rows of the DataFrame
df.shape
df.columns

df['ticker'].unique() #Get unique values in the 'ticker' column

df['ref.date'] = pd.to_datetime(df['ref.date']) #Convert 'ref.date' column to datetime format
df['ref.date'].dtypes #Check data type of 'ref.date' column

date = list(df[df.ticker == 'MSFT']['ref.date']) #Extract 'ref.date' values for ticker 'MSFT'
price = df[df.ticker == 'MSFT']['price.close'].tolist() #Extract 'price.close' values for ticker 'MSFT'

date_apple = list(df[df.ticker == 'AAPL']['ref.date']) #Extract 'ref.date' values for ticker 'MSFT'
price_apple = df[df.ticker == 'AAPL']['price.close'].tolist() #Extract 'price.close' values for ticker 'MSFT'

fig = plt.figure(figsize = (10,6)) #Create a figure object with specified size
ax = fig.add_axes([0,0,1,1]) #Add axes to the figure
ax.plot(date,price, label = "MSFT") #Plot date vs price
ax.plot(date_apple, price_apple, label = "AAPL") #Plot date vs price for Apple
ax.set_title("MSFT & AAPL closing price") #Set title of the plot
plt.legend(loc = 'upper left') #Add legend to the plot
plt.show() #Display the plot