import os
import csv
import pandas as pd

# Given my file creation on GitHub, I am getting a permission error I could not 
# solve before due date running the statement directly below
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Used a direct path to work around the issue above
csvpath = r"C:\Users\deler\Desktop\python-challenge\PyPoll\Resources\election_data.csv"
df=pd.read_csv(csvpath)

#Get a total count for the % calc
vote_count=df['Voter ID'].nunique()

#Calculate the count by candidate.  I used nunique as I am not familiar with the data set and wanted to account for possible duplicates
cc=df.groupby(['Candidate']).nunique()

#Make the %'s a whole number, as I found it easier to format around than find the syntax to hopefully format correctly
ccpercent=(cc/vote_count)*100
# Trimming the dataframes to the columns I need
candidatesvotes=cc.iloc[:,0]
candidatepercent=ccpercent.iloc[:,0]

# Joining the two tables to bring the data sets toghether, in hindsight, was not needed but it is how I got to the outcome mid development
can_sum=pd.merge(left=candidatepercent, right=candidatesvotes, how='left', left_on='Candidate', right_on='Candidate')
# Adding the index to put the candidate names back in the DF
can_sum_idx = can_sum.reset_index(drop=False)
# Sorted to have the code determine the winner
can_sum_fnl = can_sum_idx.sort_values("Voter ID_y", ascending=False)

# Defining the variables so that I can customize the print statement to match the README instructions as best as possible
can_nm1=can_sum_fnl.iloc[0,0]
can_pct1=round(can_sum_fnl.iloc[0,1],2)
can_tot1=can_sum_fnl.iloc[0,2]

can_nm2=can_sum_fnl.iloc[1,0]
can_pct2=round(can_sum_fnl.iloc[1,1],2)
can_tot2=can_sum_fnl.iloc[1,2]

can_nm3=can_sum_fnl.iloc[2,0]
can_pct3=round(can_sum_fnl.iloc[2,1],2)
can_tot3=can_sum_fnl.iloc[2,2]

can_nm4=can_sum_fnl.iloc[3,0]
can_pct4=round(can_sum_fnl.iloc[3,1],2)
can_tot4=can_sum_fnl.iloc[3,2]

print("     ")
print('Election Results')
print('-------------------')
print(f'Total Votes: {vote_count} ')
print('-------------------')
print(f'{can_nm1}: {can_pct1}% ({can_tot1})')
print(f'{can_nm2}: {can_pct2}% ({can_tot2})')
print(f'{can_nm3}: {can_pct3}% ({can_tot3})')
print(f'{can_nm4}: {can_pct4}% ({can_tot4})')
print('-------------------')
print(f'Winner: {can_nm1}')
print('-------------------')

outputPath=r"C:\Users\deler\Desktop\python-challenge\PyPoll\Analysis\Output.txt"
with open(outputPath, 'w', newline='') as txtfile:
    txtfile.write('     \n')
    txtfile.write('Election Results\n')
    txtfile.write('-------------------\n')
    txtfile.write(f'Total Votes: {vote_count}\n')
    txtfile.write('-------------------\n')
    txtfile.write(f'{can_nm1}: {can_pct1}% ({can_tot1})\n')
    txtfile.write(f'{can_nm2}: {can_pct2}% ({can_tot2})\n')
    txtfile.write(f'{can_nm3}: {can_pct3}% ({can_tot3})\n')
    txtfile.write(f'{can_nm4}: {can_pct4}% ({can_tot4})\n')
    txtfile.write('-------------------\n')
    txtfile.write(f'Winner: {can_nm1}\n')
    txtfile.write('-------------------\n')
    txtfile.close()




