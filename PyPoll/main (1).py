#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
import os

# Set path for file
csvpath=os.path.join("Resources", "election_data.csv")


# In[6]:


#Begin counting number of votes at 0. Create empty dictionary to store unique candidates' information
totalvotes=0
candidates={}
    
# Open the CSV
with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)

    #Calculate the overall total number of votes
    for row in csvreader:
        totalvotes+=1
        
        #Find unique candidate names and tally their number of votes
        if row[2] in candidates:
            candidates[row[2]]=candidates[row[2]]+1
        else:
            candidates[row[2]]=1
            


# In[7]:


mostvotes=0
mostname=0

print(f"Election Results")
print("----------------------")
print(f"Total Votes: {int(totalvotes)}")
print("----------------------")
#Calculate the percentage of votes each candidate won
for name in candidates:
    percentagevote=candidates[name]/totalvotes
    
    print(f"{name}: {percentagevote:.3%} ({candidates[name]})")
   
    #Calculate the winner based on the number of votes they won
    if mostvotes < candidates[name]:
        mostvotes=candidates[name]
        mostname=name
    
    
print("----------------------")
print(f"Winner: {mostname}")
print("----------------------")


# In[8]:


with open("PyPollResults.txt", "a") as csvfile:
    print(f"Election Results", file=csvfile)
    print("----------------------", file=csvfile)
    print(f"Total Votes: {int(totalvotes)}", file=csvfile)
    print("----------------------", file=csvfile)
    
    for name in candidates:
        percentagevote=candidates[name]/totalvotes

        print(f"{name}: {percentagevote:.3%} ({candidates[name]})", file=csvfile)

        
        if mostvotes < candidates[name]:
            mostvotes=candidates[name]
            mostname=name
    print("----------------------", file=csvfile)
    print(f"Winner: {mostname}", file=csvfile)
    print("----------------------", file=csvfile)


# In[ ]:




