import os
import csv
import pandas as pd

# Given my file creation on GitHub, I am getting a permission error I could not 
# solve before due date running the statement directly below
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = r"C:\Users\deler\Desktop\python-challenge\PyBank\Resources\budget_data.csv"
df=pd.read_csv(csvpath)

# Adding a change column to my data frame using the P&L column
df['Change']=df['Profit/Losses'] - df['Profit/Losses'].shift(1)

# Doing the average, min, and max calculations using df's
average=df['Change'].mean()
maxvalue=df['Change'].max()
maxindex=df['Change'].idxmax()
maxmonth=df.loc[maxindex,'Date']

minvalue=df['Change'].min()
minindex=df['Change'].idxmin()
minmonth=df.loc[minindex,'Date']

# I tried to do these assignments without pandas but could not get creative enough from our coursework
# After many google searches, everyone was indicating to use pandas so I switched my approach
# I kept the non-pandas approach as it was working

with open(csvpath) as csvfile:

    # CSV reader used to declare delimiter and variable that holds contents into a variable I can reference
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first, so it could be skipped
    csv_header = next(csvreader)

    # Declared the variables for the For loop below
    row_count=0
    Sum=0.0
    PandL=0.0

    for row in csvreader:

        PandL = float(row[1])
        Sum += PandL
        row_count+=1
  
# run the print as README defined

    print('Financial Analysis')
    print('-------------------')
    print(f'Total Months: {row_count}')
    print(f'Total P&L: ${Sum}')
    print(f'Average Change: ${round(average,2)}')
    print(f'Greatest Increase in Profits: {maxmonth} ${maxvalue}')
    print(f'Greatest Decrease in Profits: {minmonth} ${minvalue}')

# Pushing out the text file
    outputPath=r"C:\Users\deler\Desktop\python-challenge\PyBank\Analysis\Output.txt"
    with open(outputPath, 'w', newline='') as txtfile:
        txtfile.write('Financial Analysis\n')
        txtfile.write('-------------------\n')
        txtfile.write(f'Total Months: {row_count}\n')
        txtfile.write(f'Total P&L: ${Sum}\n')
        txtfile.write(f'Average Change: ${round(average,2)}\n')
        txtfile.write(f'Greatest Increase in Profits: {maxmonth} ${maxvalue}\n')
        txtfile.write(f'Greatest Decrease in Profits: {minmonth} ${minvalue}\n')
        txtfile.close()



