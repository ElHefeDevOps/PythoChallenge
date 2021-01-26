import csv
import os

# row_count=0
# total_sum=0
total_net=0
total_months=0
greatest_increase=["",0]
greatest_decrease=["",9999999]
net_change_list=[]
monthly_change=[]

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
        net_change_list += [net_change]
        monthly_change +=[row[0]]

# Calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

# # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    
# # Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)

# # Greatest increase in profits
#         monthly_change=int(row[1])-last_month_value
#         total_change += monthly_change
#         greatest_increase=max(greatest_increase,monthly_change)

# # Greatest decrease in profits
#         monthly_change=int(row[1])-last_month_value
#         total_change += monthly_change
#         greatest_decrease=min(greatest_decrease,monthly_change)

   
# # Gen Output Summary Financial Analysis
output = (    
f"Financial Analysis\n"    
f"----------------------------\n"    
f"Total Months: {total_months}\n"    
f"Total: ${total_net}\n"    
f"Average  Change: ${net_monthly_avg:.2f}\n"    
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"   
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


 
output_path = os.path.join("Analysis", "Analysis_File.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Initialize csv.writer
    txtfile.write(output)

# Print Statements

# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: {len(total_months)}")
# print(f"Total: ${sum(total_net)}")
# print(f"Average Change: {round(sum(net_change)/len(net_change),2)}")
# print(f"Greatest Increase in Profits: {total_months[greatest_increase]} (${(str(greatest_increase))})")
# print(f"Greatest Decrease in Profits: {total_months[greatest_decrease]} (${(str(greatest_decrease))})")


# #