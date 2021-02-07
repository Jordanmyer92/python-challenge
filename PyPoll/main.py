import os
import csv
#total number of votes cast
total_votes = 0
#complete list of candidates who received vote

#percentage of votes each candidate won

# total number of votes each candidate won

# winner ofelection based on votes



file_path = "./Resources/election_data.csv"

with open(file_path) as csvfile:

   csvreader = csv.reader(csvfile)
    
   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")
  
   for row in csvreader:
      #total number of votes cast
      total_votes=total_votes+1
      Voter_ID=row[0]
      County=row[1]
      Candidate=row[2]

      #net total amount of "profit/loses" over the enite period
      #total_profit_loss= (profit + 1)

      #calculate the changes in "profit/loses" over the enitre period then find the average of those changes
      #average_profit_loss =(profit+1) // (total_months+1)

      # greatest increase in profits (date and amount) over the entire period
     # if (profit > greatest_increase["amount"]):
       #     greatest_increase["date"] = date 
        #    greatest_increase["amount"] = profit

      # greatest decrease in loses (date and amount) over the entire period 
     # if(profit < greatest_decrease["amount"]):
         #   greatest_decrease["date"]=date 
         #   greatest_decrease["amount"]=profit   
            
       
      




#print results
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
#print(f"Net Total Proft/Loss: ${total_profit_loss}")
#print(f"Average Change: ${average_profit_loss}")
#print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
#print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")