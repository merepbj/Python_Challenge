#Your task is to create a Python script that analyzes the records to calculate each of the following:
#Import Library
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Define the function and have it accept the 'budget_data' as its sole parameter

  #* The greatest increase in profits (date and amount) over the entire period

  #* The greatest decrease in losses (date and amount) over the entire period



#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


    # Prompt the user for what record they would like to search for
    # record_to_check = input("What record do you want to look for? ")
    count = 0

    # Loop through the data
    for row in csvreader:
        count += 1

    # pl is the total net sum of profit and losses
    pl = 0
    for row in csvreader:
        pl += int(row[1])

    # adds all values in the second column to an array so we can analyze easier
    # this contains all the values in the second column
    profit_loss = []
    for row in csvreader:
        profit_loss.append(int(row[1]))

    # record the difference between the next row and the current row
    change = 0
    differences = []
    for i in range(len(profit_loss) - 1):
        change = profit_loss[i + 1] - profit_loss[i]
        differences.append(change)

    # to find sum of everything inside differences (dsum) and then find average
    dsum = 0
    for i in differences:
        dsum += i

    average = dsum/86
        
      