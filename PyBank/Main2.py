import csv
import os

row_count=0
total_sum=0
total_net=0
total_months=0
greatest_increase=[]
greatest_decrease=[]
net_change=[]

# first_row=next(reader)
# last_month_value=first_row[1]
# row_count+=1
# total_sum+=int(row[1])

csv_file = os.path.join("Resources", "budget_data.csv")
with open(csv_file, 'r') as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)


#   the total number of months included in the dataset
    total_months += 1


    #print(row_count)

#exract first row to avoid appending Net_Change
    first_row = next(reader)
    last_month_value=first_row[1]
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


# Track total months
    for row in reader:
        total_months +=1
        total_net +=int(row[1])
   

# Track net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])

# Calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

# # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    
# # Calculate the Average Net Change
    net_monthly_avg = sum(net_change) / len(net_change)

# Greatest increase in profits
        monthly_change=int(row[1])-last_month_value
        total_change += monthly_change
        greatest_increase=max(largest_increase,monthly_change)

# Greatest decrease in profits
        monthly_change=int(row[1])-last_month_value
        total_change += monthly_change
        greatest_decrease=min(greatest_decrease,monthly_change)

   
# # Gen Output Summary Financial Analysis
# Output = ()
Total Months = 86
Total = 38382578
Average change over time = -69.20944096
# the net total amount of profit / losses over the period
Greatest increase in profits = 1170593
Greatest decrease in profits = -1196225





 