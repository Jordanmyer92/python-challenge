
import csv
total_months=0
total_profit_loss=0.00
average_profit_loss=0.00
greatest_increase={"date":"amount":0}
greatest_decrease={}


file_path = "./Resources/budget_data.csv"

with open(file_path) as csvfile:

    csvreader = csv.reader(csvfile)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
  
    for row in csvreader:
        total_months=total_months+1
        date=row[0]
        profit=float(row[1])
        if(profit >greatest_increase["amount"]  ):
           greatest_increase["date"]=date 
           greatest_increase["amount"]=profit

print("Financial Analysis")
print(f"Total Months:{total_months}")
print(f"Greatest Increase in Profits: {greatest_increase["date"]}(${greatest_increase["amount]"})