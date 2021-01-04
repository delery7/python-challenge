# print("adding a main file to PyBank")
import os
import csv

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = r"C:\Users\deler\Desktop\python-challenge\PyBank\Resources\budget_data.csv"
print(csvpath)

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
    #     # Read each row of data after the header
    for row in csvreader:
    #print(row[0] + " and " + row[1])
        #for column in row.split(','):
        PandL = float(row[1])
        Sum += PandL
        row_count+=1
        averages=Sum/row_count
    print(f'The total row count is: {row_count}')
    print(f'The total sum of columns is: {Sum}')
    print(f'The average is: {averages}')


#PandL_list=[]
#for row in csvfile:
#        PandL_list.append(row[1])

#sum_PandL=0
#for rows in csvpath:
#   sum_PandL += int(rows[1])


#print("sum_PandL")