#Importing the applications that are needed to open the resource file and calculating months
import os
import csv

#defining the path for the file
csvpath = os.path.join("..","Pypoll", "Resources", "election_data.csv")

votes = {}
total_votes = 0
candidate_vote_percentage = []
most_votes = ["",0]
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
        total_votes += 1

        if candidate not in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1

    for candidate in votes:
        candidate_votes = votes[candidate]
        candidate_vote_percentage = round(float(candidate_votes) / float(total_votes) * 100,3)    
        print(f"{candidate} : {candidate_vote_percentage}% ({candidate_votes}) ")

    # def percent(votes):
    #     return votes[candidate] / total_votes * 100
                
    for (candidate, vote) in votes.items():
        if vote > maxValue:
            maxValue = vote
            winner = candidate

    winner2= max(votes,key=votes.get)
    print(f"{winner2}")
        
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
print(f"{winner}")


# # BONUS WRITE NEW FILE IN TEXT
# # Specify the file to write to
# output_path = os.path.join("..","Pypoll", "new.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as txt_file:
#     txt_file.write("Election Results")
#         "-------------------------------------"
