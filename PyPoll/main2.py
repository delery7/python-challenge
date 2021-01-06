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

maxname=cc.max(axis=1)
#print(maxname)
#print(cc)
#print(ccpercent)
print(candidatesvotes)
#print(candidatepercent)

print("     ")
print('Election Results')
print('-------------------')
print(f'Total Votes: {vote_count}')
print('-------------------')
print(f'{candidatepercent} {candidatesvotes}')
print('-------------------')
print(f'Winner: TBD')
print('-------------------')



var=0
cand=''
candidate={}
for row in csvreader:
    if row[2] not in candidate:
        candidate[row[2]]=1
    else:
        candidate[row[2]]+=1
#Loop through using the var and and to put in the highest number, that is the winner
#
print(candidate#.different functions to return different parts of the dictionary .keys() .values() .items()
#this only does the individual counts, need a total count and then to do the math