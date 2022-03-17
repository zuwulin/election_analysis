import csv

#Variable for the file to load and the path to it
voting_file = "resources/election_results.csv"

#Open the file
with open(voting_file) as election_data:

    print(election_data)

election_data.close()