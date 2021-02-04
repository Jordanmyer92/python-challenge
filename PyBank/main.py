total_months=0
total_profit_loss=0.00
average_profit_loss=0.00
greatest_inclrease={}
greatest_decrease={}
import csv

file_path = "./Resources/budget_data.csv"

with open(file_path) as csvfile:

    csvreader = csv.reader(csvfile)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
  
    for row in csvreader:
        total_months=total_months+1
         print(row)
      

print("Financial Analysis")
print(f"Total Months:{total_months}")