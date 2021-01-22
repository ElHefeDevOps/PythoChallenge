import csv
import os

csv_file = os.path.join("Resources", "election_data.csv")
with open(csv_file, 'r') as election_data:
    reader = csv.reader(election_data)
    header = next(reader)




total_votes=0
total_candidates=0
votes=0
candidate_votes=0
popular_vote= []
