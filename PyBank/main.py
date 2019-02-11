import os
import csv

# define variables
total_months = 0
total_amount = 0
max_increase_amount = 0
best_month = 0
max_decrease_amount = 0
worst_month = 0

# open csv in named folder
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
        
    # output the number of rows in csv (not returning correct value)
    for row in csvreader:
        total_months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        total_amount = total_amount + int(row[1])

        # Calculate the average of the changes in "Profit/Losses" over the entire period
        avg_change = round((total_amount / total_months), 2)

        # Calculate the greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > int(max_increase_amount):
            best_month = row[0]
            max_increase_amount = row[1]  

        # Calculate the greates decrease in losses (date and amount) over the entire period
        if int(row[1]) < int(max_decrease_amount):
            worst_month = row[0]
            max_decrease_amount = row[1]

    # Print results
    f = open('PyBank_results.txt', 'w')

    print("Financial Analysis", file=f)
    print("-" * 25, file=f)
    print(f"Total Months: {total_months}", file=f)
    print(f"Total: $ {total_amount}", file=f) 
    print(f"Average Change: $ {avg_change}", file=f)
    print(f"Greatest Increase in Profits: {best_month} ($ {max_increase_amount})", file=f)
    print(f"Greatest Decrease in Profits: {worst_month} ($ {max_decrease_amount})", file=f)
    f.close()

    print("Financial Analysis")
    print("-" * 25)
    print(f"Total Months: {total_months}")
    print(f"Total: $ {total_amount}") 
    print(f"Average Change: $ {avg_change}")
    print(f"Greatest Increase in Profits: {best_month} ($ {max_increase_amount})")
    print(f"Greatest Decrease in Profits: {worst_month} ($ {max_decrease_amount})")