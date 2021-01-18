# Week 3 Python HW
#need total number of months 
#net total amount of Profit/Loss over enitre period
#Calculate changes in Profit/Loss over entire period and average the changes
#Geatest increase in profit (date and amount) of entire peiod (use .max)
#Greatest decrease in losses (date and amount) of entire period (use .min)

#import modules os and csv
import os
import csv

#create path file for resources
csvpath = os.path.join('Resources','budget_data.csv')

#use the improved reading method with cvs module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #read header row first
    csv_header = next(csvreader)
    #print(f"CSV Header {csv_header}")
    # come back to this code and # lines above and bellow

    #for row in csvreader:
        #print(row)

    #make variables for formulas below so it doesn't
    #have an error if it's below the for loop
    num_rows = 0
    net_total = 0
    changes =[]
    prof_loss =[]

    

            #make formula to count total months
            #num_rows = 0
    #note that this for loop can be used for all
    #the following equations.
    #retyping the for loop for ea formula does not work
    for row in csvreader:
        num_rows += 1
    #print("Total Months: " + str(num_rows))
    #make formula to calculate net total of Profit/Losses
        net_total += int(row[1])
    #print(str(net_total))
    #have append the profit/loss column in a diff list
        prof_loss.append(int(row[1]))
    #calculate average of changes in Profit/Loss
        avg_change = prof_loss / num_rows
    #print(avg_change)
    #calculate greatest increase
        max_profit = max(prof_loss)
    print(max_profit)


    

