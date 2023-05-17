# Modules
import os
import csv

# Set path for read and write file
csvpath = os.path.join("Resources", "budget_data.csv")
textpath = os.path.join("Analysis", "Financial_Analysis.txt")

# Set variables
total_months = 0
total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the csv file
with open(csvpath, encoding='UTF-8') as csvfile, open(textpath, 'w', encoding='UTF-8') as textfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvwriter = csv.writer(textfile, delimiter=",")
    header = next(csvreader)

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow([])
    csvwriter.writerow (["---------------------------"])

    # To loop through the rows in csvfile
    for row in csvreader:

        # Count the rows to calculate total months
        total_months += 1

        # Calculate the total amount of profit/loss
        profit_loss = int(row[1])
        total += profit_loss

        # Calculate the change in profit/loss
        if previous_profit_loss !=0:
            current_change = profit_loss - previous_profit_loss
            changes.append(current_change)
            

            # Check for the greatest increase and decrease in profit/loss
            if current_change > greatest_increase [1]:
                greatest_increase = [row[0], current_change]
                
            if current_change < greatest_decrease[1]:
                greatest_decrease = [row[0], current_change]
        
        previous_profit_loss = profit_loss
    average_change = sum(changes) / len(changes)

    # Write the values in textfile
    csvwriter.writerow([f"Total months: ${total_months}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average change: ${average_change}"])
    csvwriter.writerow([f"Greatest increase in profits: {greatest_increase[0]} ${greatest_increase[1]}"])
    csvwriter.writerow([f"Greatest decrease in profits: {greatest_decrease[0]} ${greatest_decrease[1]}"])

# Print the results
print("Financial Analysis")
print("-------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total}")
print(f"Average change: ${average_change}")
print(f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
