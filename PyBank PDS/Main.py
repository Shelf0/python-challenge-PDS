#import CSV File & Appropriate libraries

import csv
import os

# Set Variables & Counters
months=0
total=0
AverageChange=0
# Set Variables for Increase & Decrease
GreatestIncrease=0
GreatestIncreaseMonth=None
GreatestDecrease=0
GreatestDecreaseMonth=None


# Set the path for the python file 

csvpath="C:/Users/19739/Desktop/Data Science/RUT-SOM-DATA-PT-09-2020-U-C/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

#Lists for Data 
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # row is a list of strings, with row[0] == the data and row[1] == the profit/loss change 
        date = row[0]
        change = int(row[1])
        # record = {date: change}

        # print(row)
        months += 1
        total += change


        if (change > GreatestIncrease):
            GreatestIncrease = change
            GreatestIncreaseMonth = date
        
        if (change < GreatestDecrease):
            GreatestDecrease = change
            GreatestDecreaseMonth = date

#Calculate the Average Change 

AverageChange = str(round(total/months, 2))


# the "w" here lets me write the file out if it doesnt exist
with open("results.txt", "w") as myresults:
    myresults.write("Financial Analysis/n")
    myresults.write("-"*28 + "/n")
    myresults.write(f'Total Months: {months}/n')
    myresults.write(f'Total: ${total}/n')
    myresults.write(f'Average Change: ${AverageChange}/n')
    myresults.write(f'Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})/n')
    myresults.write(f'Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})')
    myresults.close()

#Printing out Results 
print("Financial Analysis")
print("-"*28)
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${AverageChange}')
print(f'Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})')
print(f'Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})')

