#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Modules
import csv
import os


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")


# In[4]:


num_months=0
total_months=0
total_revenue=0
revenue=[]
changes=[]
month=[]

# Open the CSV
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    #Skip the first row
    firstrow = next(csvreader)
    
    total_months+=1
    total_revenue=total_revenue+int(firstrow[1])
   
    previous_revenue=int(firstrow[1])
    

    # Loop through data
    for row in csvreader:
        total_months=total_months+1
        total_revenue+=int(row[1])
        
        revenue.append(float(row[1]))
        month.append(row[0])
        


# In[5]:


for x in range(len(revenue)):
    #calculate the average of the difference between all rows in profit/loss column
    changes.append(revenue[x]-previous_revenue)
    previous_revenue = revenue[x]
average_change=sum(changes)/(total_months)

#calculate greatest increase in profit/loss column + date associated with it
greatest_increase=max(changes)
greatest_increase_date=str(month[changes.index(max(changes))])

#calculate greatest decrease in profit/loss column + date associated with it
greatest_decrease=min(changes)
greatest_decrease_date=str(month[changes.index(min(changes))])


# In[6]:


print(f"Financial Analysis")
print("----------------------")
print(f"Total Months: {int(total_months)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${int(average_change)}")
print(f"Greatest Increase: {str(greatest_increase_date)} ${(int(greatest_increase))}")
print(f"Greatest Decrease: {str(greatest_decrease_date)} ${(int(greatest_decrease))}")


# In[7]:


with open("PyBankResults.txt", "a") as csvfile:
    print(f"Financial Analysis", file=csvfile)
    print("----------------------", file=csvfile)
    print(f"Total Months: {int(total_months)}", file=csvfile)
    print(f"Total: ${str(total_revenue)}",file=csvfile)
    print(f"Average Change: ${int(average_change)}",file=csvfile)
    print(f"Greatest Increase: {str(greatest_increase_date)} ${(int(greatest_increase))}",file=csvfile)
    print(f"Greatest Decrease: {str(greatest_decrease_date)} ${(int(greatest_decrease))}",file=csvfile)


# In[ ]:




