#Importing the applications that are needed to open the resource file and calculating months
import os
import csv

#defining the path for the file
csvpath = os.path.join("..","Pypoll", "Resources", "election_data.csv")

#Setting the initial values 
votes = {}
total_votes = 0
candidate_vote_percentage = []
maxValue = 0
winner = ""

print("Election Results")
print("-------------------------------------")

#Setting the loop for calculating the Total Votes
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        candidate = row[2]
        vote = row[0]
        
        #Counting total votes
        total_votes += 1

        #Counting the votes for each candidate
        if candidate not in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1

    #Calculating the percentage of votes for each candidate
    for candidate in votes:
        candidate_votes = votes[candidate]
        candidate_vote_percentage = round(float(candidate_votes) / float(total_votes) * 100,3)    
        print(f"{candidate} : {candidate_vote_percentage}% ({candidate_votes}) ")

    # #Alternative method to calculating the votes for each candidate
    # def percent(votes):
    #     return votes[candidate] / total_votes * 100
                
    #Identifiying the winner
    for (candidate, vote) in votes.items():
        if vote > maxValue:
            maxValue = vote
            winner = candidate

    # # Alternative way of calculating the winner with the use of max() and .get
    # winner2= max(votes,key=votes.get)
    # print(f"{winner2}")
        
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
print(f"Winner: {winner}")


# BONUS WRITE NEW FILE IN TEXT
# Specify the file to write to
output_path = os.path.join("..","Pypoll", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------------------\n")
    for candidate in votes:
        txt_file.write(f"{candidate}: {candidate_vote_percentage}% ({candidate_votes})\n")
    txt_file.write("-------------------------------------\n")
    txt_file.write(f"Winner: {winner}")

