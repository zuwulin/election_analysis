import csv
import os

#Variable for the file to load and the path to it
file_to_load = os.path.join("resources", "election_results.csv")
#Variable for the file to sova and the path to it
file_to_save = os.path.join("resources", "analysis", "election_analysis.txt")
#Total Vote Counter
total_votes = 0
#Candidate election options
candidate_options = []
#Candidate dictionary
candidate_votes = {}
#Winning candidate stats
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
#Read and skip the header row
    headers = next(file_reader)
#Print each row after the header in the CSV file
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]
#Create a list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
#Count total votes for each candidate
        candidate_votes[candidate_name] += 1
#Count vote percentage for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"--------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------\n")
    print(winning_candidate_summary)