# print("adding a main file to PyBank")
import os
import csv
import pandas as pd

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = r"C:\Users\deler\Desktop\python-challenge\PyPoll\Resources\election_data.csv"
#print(csvpath)
df=pd.read_csv(csvpath)
print(df)

vote_count=df['Voter ID'].nunique()
print(vote_count)


# difference=0.0
# df['Change']=df['Profit/Losses'] - df['Profit/Losses'].shift(1)
# average=df['Change'].mean()
# maxvalue=df['Change'].max()
# maxindex=df['Change'].idxmax()
# maxmonth=df.loc[maxindex,'Date']

# minvalue=df['Change'].min()
# minindex=df['Change'].idxmin()
# minmonth=df.loc[minindex,'Date']
# #print(df)
# with open(csvpath) as csvfile:

#     # CSV reader used to declare delimiter and variable that holds contents into a variable I can reference
#     csvreader = csv.reader(csvfile, delimiter=',')

#     # Read the header row first (skip this step if there is now header)
#     csv_header = next(csvreader)
#     # print(f"CSV Header: {csv_header}")

#     row_count=0
#     Sum=0.0
#     PandL=0.0

#     # Tried to start this without pandas, so the count and P&L Sum is done without a dataframe
#     for row in csvreader:

#         PandL = float(row[1])
#         Sum += PandL
#         row_count+=1
#        # averages=Sum/row_count


     print('Financial Analysis')
#     print('-------------------')
#     print(f'Total Months: {row_count}')
#     print(f'Total P&L: ${Sum}')
#     print(f'Average Change: ${round(average,2)}')
#     print(f'Greatest Increase in Profits: {maxmonth} ${maxvalue}')
#     print(f'Greatest Decrease in Profits: {minmonth} ${minvalue}')

#     outputPath=r"C:\Users\deler\Desktop\python-challenge\PyBank\Analysis\Output.txt"
#     with open(outputPath, 'w', newline='') as txtfile:
#         txtfile.write('Financial Analysis\n')
#         txtfile.write('-------------------\n')
#         txtfile.write(f'Total Months: {row_count}\n')
#         txtfile.write(f'Total P&L: ${Sum}\n')
#         txtfile.write(f'Average Change: ${round(average,2)}\n')
#         txtfile.write(f'Greatest Increase in Profits: {maxmonth} ${maxvalue}\n')
#         txtfile.write(f'Greatest Decrease in Profits: {minmonth} ${minvalue}\n')
#         txtfile.close()



