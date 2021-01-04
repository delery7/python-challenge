# print("adding a main file to PyBank")
import os
import csv
import pandas as pd

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = r"C:\Users\deler\Desktop\python-challenge\PyBank\Resources\budget_data.csv"
#print(csvpath)
df=pd.read_csv(csvpath)

difference=0.0
df['Change']=df['Profit/Losses'] - df['Profit/Losses'].shift(1)
average=df['Change'].mean()
#max=df[df['Profit/Losses']==df['Profit/Losses'].max()]
#max=df.groupby(['Date','Profit/Losses'], as_index=False)['Profit/Losses'].max()
maxvalue=df['Profit/Losses'].max()
maxindex=df['Profit/Losses'].idxmax()
maxmonth=df.loc[maxindex,'Date']

minvalue=df['Profit/Losses'].min()
minindex=df['Profit/Losses'].idxmin()
minmonth=df.loc[minindex,'Date']
#print(df)
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    row_count=0
    averages=0.0
    Sum=0.0
    PandL=0.0
    change=0.0
    #     # Read each row of data after the header
    for row in csvreader:
    #print(row[0] + " and " + row[1])
        #for column in row.split(','):
        PandL = float(row[1])
        Sum += PandL
        row_count+=1
       # averages=Sum/row_count
    # for i, rows in csvreader:
    #     for j,rows in csvreader:
    #        change= rows[j]-rows[i-1]
    #     print(rows[j])

    
    print(round(average,2))
    print(maxvalue)
    print(maxindex)
    print(maxmonth)
    print(f'{minvalue} {minmonth}')
    print(f'The total row count is: {row_count}')
    print(f'The total sum of columns is: {Sum}')
    print(f'Change is {change}')



