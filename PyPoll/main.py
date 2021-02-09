import os
import csv
#total number of votes cast
total_votes = 0
#complete list of candidates who received vote
candidates_list = {}
#percentage of votes each candidate won
percent_of_votes = 0.00
# total number of votes each candidate won
total_votes_per = 0.00
# winner ofelection based on votes



file_path = "./Resources/election_data.csv"

with open(file_path) as csvfile:

   csvreader = csv.reader(csvfile)
    
   csv_header = next(csvreader)
   #print(f"CSV Header: {csv_header}")
   #complete list of candidates who received vote
   #Candidate= csv_header.index("Candidate")
   
   
   for row in csvreader:
      #total number of votes cast
      total_votes=total_votes+1
   
      #complete list of candidates who received vote
      Candidate=row[2]
      
         
      
      #percentage of votes each candidate won
      #percent_of_votes = (Candidate) // (total_votes+1)

      # total number of votes each candidate won
      #total_votes_per  

      # winner ofelection based on votes
     
            
       
      




#print results
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")
print(f"{Candidate} {percent_of_votes} {total_votes_per}")
print
#print(f"names: {percent_of_votes}")
#print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


