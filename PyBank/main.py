import os
import csv

#create blank lists for data
Months=[]
pnl_change=[]
mydict={}

#read CSV file
csvpath=os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
#populate lists
    csv_header=next(csvreader)
    for row in csvreader:
        Months.append(row[0])
        pnl_change.append(int(row[1]))

    #calculate total months
    sum_months=len(Months)
    print(sum_months)

    #calculate net profit/loss over period
    net_pnl=sum(pnl_change)
    print(net_pnl)

    #calculate avg of pnl changes over period
    def Average(sum,length):
        return(sum/length)
    avg_pnl=Average(net_pnl,sum_months)
    print(avg_pnl)

    #calculate greatest increase
    max_profit=max(pnl_change)
    print(max_profit)

    #calculate greatest loss
    max_loss=min(pnl_change)
    print(max_loss)

    #find month of max profit
    print(pnl_change.index(max_profit))
    max_month=Months[pnl_change.index(max_profit)]
    print(max_month)

    #find month of max loss
    print(pnl_change.index(max_loss))
    min_month=Months[pnl_change.index(max_loss)]
    print(min_month)

    #print results
    






