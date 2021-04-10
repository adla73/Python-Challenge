# import modules / dependencies

import os           #os to join elements of the file path for PC or Mac
import csv          #read csv file using .reader method

csv_file_path = os.path.join("budget_data.csv")

file_to_output = os.path.join("Analysis", "Bank_Data_Analysis.txt")
# print(csv_file_path)

# initialize variables
total_months = 0
total = 0
row = 0
current_month = 0
total_months = 0
previous_month_net = 0 
avg_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]
net_change_list = []


# open and read the csv_file called budget_data.py
with open(Budget_data) as csv_file
    csv_reader = csv.reader(csv_file, delimiter= ",")

    # read the header
    csv_header = next(csv_reader)
    
    # Setup previous net
    first_row = next(csv_reader)
    previous_month_net = int(first_row[1])
    total_months += 1
    total = int(first_row[1])

        
    for row in csv_reader:

        # Get total_months and total
        total_months += 1
        total += int(row[1])



        # Get net_change
        current_net = int(row[1])
        net_change = current_net - previous_month_net
        net_change_list += [net_change] 

        #swap previoius month net
        previous_month_net = current_net




        #Determine greatest_increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change


        #Determine greatest_decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#Calculate net_change
    #formula will be = average_change = sum(net_change) / (months - 1)
    average_change = Round(sum(net_change_list) / (total_months),2)



# --------------------------------------------------------------------------------------
#create summary table
Summary_Table_output = (
    f""
    f"Financial Analysis"
    f"------------------"
    f"Total Months: {total_months}"
    f"Total: {total}"
    f"Average Change: {avg_change}"
    f"Greatest Increase in Profits: {greatest_increase}"
    f"Greatest Decrease in Profits: {greatest_decrease}"


)


