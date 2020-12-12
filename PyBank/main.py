# Dependencies
import csv
import os
# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")


total_months = 0
total_profit = 0
previousNum = 0
profit_losses = []
sum_of_pl = 0
net_change = 0
greatest_increase = 0
increase_month = ""
greatest_decrease = 0
decrease_month = ""
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # Read the header row
    header = next(reader)
    first_row = next(reader)
    previousNum = int(first_row[1]) #867884
    total_profit = int(first_row[1])
    for row in reader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        #net-changes
        net_change = previousNum - int(row[1])
        profit_losses.append(int(row[1]) - previousNum) # -69417 - 310503
        previousNum = int(row[1])
         # -379920
        if net_change > greatest_increase: # -379920 > 662642
            greatest_increase = net_change
            increase_month = row[0]
        if net_change < greatest_decrease: # -379920 < -116771
            greatest_decrease = net_change
            decrease_month = row[0] # May-2010
for x in profit_losses:
    sum_of_pl = sum_of_pl + x
print(total_months)
print(profit_losses)
print(sum_of_pl/len(profit_losses))
print(total_profit) #38382578
print(max(profit_losses))
print(min(profit_losses))
print(greatest_increase, increase_month)
print(greatest_decrease, decrease_month)
print("-------------------------")


# Specify the file to write to
output_path = os.path.join("Analysis", "new.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='', encoding = "UTF-8") as txtfile:
    print(total_months)
    print(profit_losses)
    print(sum_of_pl/len(profit_losses))
    print(total_profit) #38382578
    print(max(profit_losses))
    print(min(profit_losses))
    print(greatest_increase, increase_month)
    print(greatest_decrease)
    print("-------------------------")
    print(increase_month)
    print(decrease_month)
