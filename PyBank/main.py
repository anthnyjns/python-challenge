import os
import csv

# open csv in named folder
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # These initial print commands are for testing - comment out once completed
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

    # ------- main section -------

    print("Financial Analysis")
    print("----------------------------------")

    # output the number of rows in csv (not returning correct value)
    csv_data = list(csvreader)
    print("Total Months: " + str(sum(csv_data)))


    # ------- scratch code section / remove when completed -------
    
    # data = list(csvreader)
    # row_count = len(data)
    # print(row_count)

    # total_months = sum(1 for row in csvreader)
    # print(total_months)

    # ------- end scratch code section -------


    # Calculate the net total amount of "Profit/Losses" over the entire period
    total_amount = sum(csvreader[1])
    print("Total: " + "$" + "(total_amount)")

    # Calculate the average of the changes in "Profit/Losses" over the entire period


    # Calculate the greatest increase in profits (date and amount) over the entire period


    # Calculate the greates decrease in losses (date and amount) over the entire period