import os
import csv
#total number of months in the data set
total_months = 0
#net total amount of "profit/loses" over the enite period
total_profit_loss = 0.00
#calculate the changes in "profit/loses" over the enitre period then find the average of those changes
average_profit_loss = 0.00
# greatest increase in profits (date and amount) over the entire period
greatest_increase={"date":"", "amount":0}
# greatest decrease in loses (date and amount) over the entire period
greatest_decrease={"date":"", "amount":0}


file_path = "./Resources/budget_data.csv"

with open(file_path) as csvfile:

   csvreader = csv.reader(csvfile)
    
   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")
  
   for row in csvreader:
      #total number of months in the data set
      total_months=total_months+1
      date=row[0]
      profit=float(row[1])

      #net total amount of "profit/loses" over the enite period
      total_profit_loss= (profit + 1)

      #calculate the changes in "profit/loses" over the enitre period then find the average of those changes
      average_profit_loss =(profit+1) // (total_months+1)

      # greatest increase in profits (date and amount) over the entire period
      if (profit > greatest_increase["amount"]):
            greatest_increase["date"] = date 
            greatest_increase["amount"] = profit

      # greatest decrease in loses (date and amount) over the entire period 
      if(profit < greatest_decrease["amount"]):
            greatest_decrease["date"]=date 
            greatest_decrease["amount"]=profit   
            
       
      




#print results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Proft/Loss: ${total_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
