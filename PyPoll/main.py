import os
import csv
#total number of votes cast
total_votes = 0
#complete list of candidates who received vote
candidates_list = {"Candidate":""}
#percentage of votes each candidate won
percent_of_votes = 0.00
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

      #complete list of candidates who received vote
      

      #percentage of votes each candidate won
      #percent_of_votes = (Candidate+1) // (total_votes+1)

      # total number of votes each candidate won
   

      # winner ofelection based on votes
     
            
       
      




#print results
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")
print(f"Candidate: {candidates_list['Candidate']} ") 
#print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
#print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


