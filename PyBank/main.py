import os
import csv

#create blank lists for data
Months=[]
pnl_change=[]
total_pnl=[]
avgchange=[]
maxincrease=[]


#read CSV file
csvpath=os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
#populate lists
    csv_header=next(csvreader)
    for row in csvreader:
        Months.append(row[0])
        pnl_change.append(row[1])

print(Months)
