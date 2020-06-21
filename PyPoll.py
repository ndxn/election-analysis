# Data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Import CSV
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('/Users/Neal/DataAustin2020/Challenges/election-analysis/Resources/election_results.csv')

# Open the election results and read the file.
with open(file_to_load) as election_data:



# To do: perform analysis.
    print(election_data)
# # Close the file.
#     election_data.close()