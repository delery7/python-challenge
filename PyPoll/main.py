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
#provide column names to the DF's, then join on Candidate, then print each element independently
# put print statements in a for loop as another idea
can_sum=pd.merge(left=candidatepercent, right=candidatesvotes, how='left', left_on='Candidate', right_on='Candidate')
can_sum_idx = can_sum.reset_index(drop=False)
can_sum_fnl = can_sum_idx.sort_values("Voter ID_y", ascending=False)


# print(can_sum_idx)
# print(can_sum_fnl)

#print(cc)
#print(ccpercent)
#print(candidatesvotes)
#print(candidatepercent)
#print(can_sum)

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





