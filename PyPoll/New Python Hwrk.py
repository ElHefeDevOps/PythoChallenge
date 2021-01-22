#New PyHwrk
import csv 
with open('Resources/election_data.csv', 'r') as my_data
    reader=csv.reader(my_data)
    header=next(reader)
    print(header)
    