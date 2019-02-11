import os
import csv

# define variables
total_votes_cast = 0
list_of_candidates = []
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0
winning_vote_tally = 0
winner = []

# open csv in named folder
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)

        # Calculate the Total Number of Votes Cast        
        total_votes_cast += 1

        # Create a list of all Candidates receiving votes
        candidate_name = row[2]

        if candidate_name not in list_of_candidates:
            list_of_candidates.append(candidate_name)

        # Calculate the Total Number of Votes each candidate won
        if candidate_name == list_of_candidates[0]:
            candidate1_votes += 1

        elif candidate_name == list_of_candidates[1]:
            candidate2_votes += 1

        elif candidate_name == list_of_candidates[2]:
            candidate3_votes += 1

        elif candidate_name == list_of_candidates[3]:
            candidate4_votes += 1
        
        # Calculate the % of votes each candidate received
        per_vote_candidate1 = "{:.3%}".format(candidate1_votes / total_votes_cast)
        per_vote_candidate2 = "{:.3%}".format(candidate2_votes / total_votes_cast)
        per_vote_candidate3 = "{:.3%}".format(candidate3_votes / total_votes_cast)
        per_vote_candidate4 = "{:.3%}".format(candidate4_votes / total_votes_cast)

# Determine the winner
if candidate1_votes > winning_vote_tally:
    winning_vote_tally = candidate1_votes
    winner = list_of_candidates[0]

if candidate2_votes > winning_vote_tally:
    winning_vote_tally = candidate2_votes
    winner = list_of_candidates[1]
        
if candidate3_votes > winning_vote_tally:
    winning_vote_tally = candidate3_votes
    winner = list_of_candidates[2]
        
if candidate4_votes > winning_vote_tally:
    winning_vote_tally = candidate4_votes
    winner = list_of_candidates[3]       
        
# Print election results
f = open('PyPoll.txt', 'w')

print("Election Results", file=f)
print("-" * 25, file=f)
print("Total Votes: " + str(total_votes_cast), file=f)
print("-" * 25, file=f)
print((list_of_candidates[0]) + ": " + (per_vote_candidate1) + " ("+ str(candidate1_votes) + ")", file=f)
print((list_of_candidates[1]) + ": " + (per_vote_candidate2) + " ("+ str(candidate2_votes) + ")", file=f)
print((list_of_candidates[2]) + ": " + (per_vote_candidate3) + " ("+ str(candidate3_votes) + ")", file=f)
print((list_of_candidates[3]) + ": " + (per_vote_candidate4) + " ("+ str(candidate4_votes) + ")", file=f)
print("-" * 25, file=f)
print("Winner: "+ (winner), file=f)
print("-" * 25, file=f)
f.close()


print("Election Results")
print("-" * 25)
print("Total Votes: " + str(total_votes_cast))
print("-" * 25)
print((list_of_candidates[0]) + ": " + (per_vote_candidate1) + " ("+ str(candidate1_votes) + ")")
print((list_of_candidates[1]) + ": " + (per_vote_candidate2) + " ("+ str(candidate2_votes) + ")")
print((list_of_candidates[2]) + ": " + (per_vote_candidate3) + " ("+ str(candidate3_votes) + ")")
print((list_of_candidates[3]) + ": " + (per_vote_candidate4) + " ("+ str(candidate4_votes) + ")")
print("-" * 25)
print("Winner: "+ (winner))
print("-" * 25)