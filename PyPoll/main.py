import os
import csv
#total number of votes cast
total_votes = 0
#complete list of candidates who received vote
candidates_list = {}
candidate = ""
#percentage of votes each candidate won
percent_of_votes = 0.00
# total number of votes each candidate won
total_votes_per = 0.00
# winner ofelection based on votes



file_path = "./Resources/election_data.csv"

with open(file_path) as csvfile:

   csvreader = csv.reader(csvfile)
    
   csv_header = next(csvreader)
 
   #complete list of candidates who received vote
  
   
   
   for row in csvreader:
      #total number of votes cast
      total_votes=total_votes+1
   
      #complete list of candidates who received vote
      candidate = row[2]
      if candidate in candidates_list:
         candidates_list[candidate]+=1
      else:
         candidates_list[candidate]=1 
         
      
      #percentage of votes each candidate won
      

      # total number of votes each candidate won
      #total_votes_per  

      # winner ofelection based on votes
      winner = ("", 0)
            
       
      




#print results
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-------------------")
for key, value in candidates_list.items():
   print(f"{key}: {round(value/total_votes *100, 2)}00% ({value})")
   if value > winner[1]:
      winner=(key,value)
print("-------------------")
print(f"Winner: {winner[0]}")



