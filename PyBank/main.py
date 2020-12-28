# print("adding a main file to PyBank")
import os
import csv

# csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = 'c:/Users/deler/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
row_count=0
    # Read each row of data after the header
for row in csvpath:
    row_count+=1
print(f'The total row count is: {row_count}')


sum_PandL=0
for rows in csvpath:
   sum_PandL += int(rows[1])


#print("sum_PandL")