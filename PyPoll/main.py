# print("adding a main file to PyBank")
import os
import csv
import pandas as pd


#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = r"C:\Users\deler\Desktop\python-challenge\PyPoll\Resources\election_data.csv"
#print(csvpath)
df=pd.read_csv(csvpath)
#print(df)

vote_count=df['Voter ID'].nunique()
# print(vote_count)
cc=df.groupby(['Candidate']).nunique()
ccpercent=(cc/vote_count)*100
candidatesvotes=cc.iloc[:,0]
candidatepercent=ccpercent.iloc[:,0]

maxname=cc.max(axis=1)
print(maxname)
#print(cc)
# print(ccpercent)
# print(candidatesvotes)
# print(candidatepercent)

print("     ")
print('Election Results')
print('-------------------')
print(f'Total Votes: {vote_count}')
print('-------------------')
print(f'{candidatepercent} {candidatesvotes}')
print('-------------------')
print(f'Winner: TBD')
print('-------------------')

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



