import os
import csv

#create blank lists for data
Months=[]
pnl=[]

#read CSV file
csvpath=os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
#populate lists
    csv_header=next(csvreader)
    for row in csvreader:
        Months.append(row[0])
        pnl.append(int(row[1]))
        

    #calculate total months
    sum_months=len(Months)
   
    #calculate net profit/loss over period
    net_pnl=sum(pnl)
    
    #calculate avg of pnl changes over period

    pnl_change=[]
    for i in range(len(pnl)-1):
        pnl_change.append(pnl[i+1]-pnl[i])
   
    sum_pnl_change=sum(pnl_change)
    
    def Average(sum,length):
        return(sum/length)
    avg_pnl=Average(sum_pnl_change,sum_months-1)
    

    #calculate greatest increase
    max_profit=max(pnl_change)
    
    #calculate greatest loss
    max_loss=min(pnl_change)
    
    #find month of max profit
    max_month=Months[(pnl_change.index(max_profit))+1]
    
    #find month of max loss
    min_month=Months[(pnl_change.index(max_loss))+1]
    
#print results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {sum_months}")
print(f"Total: {net_pnl}")
print(f"Average  Change: ${avg_pnl}")
print(f"Greatest Increase in Profits: {max_month} ${max_profit}")
print(f"Greatest Decrease in Profits: {min_month} ${max_loss}")

#export text file
output_path=os.path.join("Analysis","Fiancial_Analysis.csv")
with open(output_path,'w') as csvfile2:
    csvwriter=csv.writer(csvfile2,delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Total Months: ',sum_months])
    csvwriter.writerow(['Total: $',net_pnl])
    csvwriter.writerow(['Average Change: $',avg_pnl])
    csvwriter.writerow(['Greatest Increase in Profits: ',max_month,max_profit])
    csvwriter.writerow(['Greatest Decrease in Profits: ',min_month,max_loss])







