import os
import csv

candidates={}

#import csv file
csvpath=os.path.join('Resources','election_data.csv')

#get total votes
with open(csvpath) as election_votes:
    csvreader=csv.reader(election_votes,delimiter=',')
    csv_header=next(election_votes)

    total_votes=len(list(csvreader))

#create dictionary of each candidate recieving a vote
#populate using for loop adding value to each candidate 

with open(csvpath) as election_votes:
    csvreader=csv.reader(election_votes,delimiter=',')
    csv_header=next(election_votes)
    
    for row in csvreader:
        if (row[2] not in candidates):
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

#percentage of votes for each candidate
cand_list=list(candidates.keys())

#determine winner
winner=max(candidates,key=candidates.get)

#print to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes : {total_votes}")
print("--------------------------")
for i in cand_list:
    print(f"{i} : {format((candidates[i]/total_votes),'.1%')} ({candidates[i]})")
print("---------------------------")
print(f"Winner: {winner}")

#export csv
output_path=os.path.join("Analysis","Election_Results.csv")
with open(output_path,'w') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow(['Total Votes: ',total_votes])
    csvwriter.writerow(['------------------------------'])
    for i in cand_list:
        csvwriter.writerow([i,candidates[i]/total_votes,candidates[i]])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow(['Winner: ',winner])

