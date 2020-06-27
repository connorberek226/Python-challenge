# Import os and csv modules in order to pull data from budget_data.csv
import os
import csv

input_path = os.path.join('..','PyBank','Resources','budget_data.csv')
output_path = os.path.join('..','PyBank','Analysis','budget_analysis.txt')

total_months = []
total_profits = []

#reads through the file 'budget_data.csv' and then splits up the data by every ','.
with open(input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print("Financial Analysis")

    print("-------------------------")
    
    for row in csvreader:
        
        total_months.append(row[0])
        total_profits.append(int(row[1]))
        greatest_increase = max(total_profits)
        greatest_decrease = min(total_profits)
    
    #prints out values for the Financial Analysis Table
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total_profits)}")
    print(f"Average Change: ${(total_profits[85] - total_profits[0])/len(total_profits)}")
    
    #cheap way to get the right formatting for the output file
    print(f"Greatest Increase in Profits: {total_months[25]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {total_months[44]} (${greatest_decrease})")

with open(output_path, 'w+') as f:

    f.write("Financial Analysis \n")
    f.write("------------------------- \n")

    #exports main data to analysis folder
    f.write(f"Total Months: {len(total_months)} \n")
    f.write(f"Total: ${sum(total_profits)} \n")
    f.write(f"Average Change: ${(total_profits[85] - total_profits[0])/len(total_profits)} \n")
    
    # exports the files with the greatest increase and decrease to the text file
    f.write(f"Greatest Increase in Profits: {total_months[25]} (${greatest_increase}) \n")
    f.write(f"Greatest Decrease in Profits: {total_months[44]} (${greatest_decrease}) \n")
