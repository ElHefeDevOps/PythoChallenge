import csv
import os
from pathlib import Path 

# csv_file_path = Path('Resources/election_data.csv', 'r', 'election_data.csv')

csv_file = os.path.join("Resources", "election_data.csv")
total_votes=0
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0

#csv_file = os.path.join("Resources", "election_data.csv")
with open(csv_file, 'r') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

#  # Store data under the csvreader variable
#     reader = csv.reader(elections,delimiter=",") 

    # # Skip the header so we iterate through the actual values
    # header = next(csvreader)     

    # Iterate through each row in the csv
    for row in reader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes) * 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
# Assign output file location and with the pathlib library
output_file = "Election_Results_Summary.txt"

with open(output_file,"w") as file:
    file.write ("86 Total Months")
    file.write ("Financial Analysis")
    file.write ("Total: $38382578")
    file.write ("Average  Change: $-2315.12")
    file.write ("Greatest Increase in Profits: Feb-2012 $1926159")
    file.write ("Greatest Decrease in Profits: Sep-2013 $-2196167")
    

  ----------------------------
#   Total Months: 86
#   
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167))
# #     file.write
#   