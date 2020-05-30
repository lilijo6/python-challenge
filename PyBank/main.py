#Importing the applications that are needed to open the resource file and calculating months
import os
import csv
import statistics
#import datetime

#defining the path for the file
csvpath = os.path.join("..","Pybank", "Resources", "budget_data.csv")

#Creating list with initial values for the variables
Total_Months = 0
Net_Total = 0
avg_change = 0
net_change = []
Greatest_Increase = ["",0]
Greatest_Decrease = ["",999999999999]

# #Calculating the total number of months manually
# end_date = datetime.datetime(2017,2,1)
# start_date = datetime.datetime(2010, 1, 1)

# Total_Months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

#Opening the data file in read mode
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    #skips the header
    next(csvreader)

    #Initializing the variables so that delta can be calculated and those first variables are still included
    firstrow = next(csvreader)    
    previous_net = int(firstrow[1])
    Total_Months = 1
    Net_Total = Net_Total + int(firstrow[1])
    
    #Setting the loop for iterating through the rows in the file
    for row in csvreader:
        #Total number of months equals the number of rows
        Total_Months += 1
        #Adding all the values in the column for Profit/Losses
        Net_Total += int(row[1])
        #calculating the difference between the previous Profit/Loss to get change(delta)
        delta = int(row[1])-previous_net
        #appending all 
        previous_net = int(row[1])
        net_change.append(delta)

        #Conditional statement to check for the greatest value and lowest value       
        if delta > Greatest_Increase[1]:
            Greatest_Increase[0]=row[0]
            Greatest_Increase[1]=delta

        if delta < Greatest_Decrease[1]:
            Greatest_Decrease[0]=row[0]
            Greatest_Decrease[1]=delta
          
    #Clculating Average
    avg_change = round(sum(net_change)/len(net_change),2)
   
output =(
    "Financial Analysis\n"
    "\n--------------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Net Total: ${Net_Total}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase: ${Greatest_Increase[1]} Date {Greatest_Increase[0]}\n"
    f"Greatest Decrease: ${Greatest_Decrease[1]} Date {Greatest_Decrease[0]}\n")

#Prints to GitBash
print(output)

# # BONUS WRITE NEW FILE IN TEXT
# # Specify the file to write to
output_path = os.path.join("..","Pybank", "new.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txt_file:
 txt_file.write(output)

#     # Write the first row (column headers)
#     csvwriter.writerow(['Total Months', ""])

#     # Write the second row
#     csvwriter.writerow(['Total', '', ''])

#     # Write the second row
#     csvwriter.writerow(['Average change', '', ''])
#     csvwriter.writerow(['Greatest Increase ', '', ''])
#     csvwriter.writerow(['Greatest Decrease ', '', ''])

# # Generate Output Summary
# output = (
#     f"Financial Analysis\n"
#     f"----------------------------\n"
#     f"Total Months: {total_months}\n"
#     f"Total: ${total_net}\n"
#     f"Average  Change: ${net_monthly_avg:.2f}\n"
#     f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
#     f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# # Print the output (to terminal)
# print(output)
# # Export the results to text file
# with open(file_to_output, "w") as txt_file:
#     txt_file.write(output)