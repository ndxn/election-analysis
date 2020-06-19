# Data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Import CSV
import csv

# Import the datetime class from the datetime module.
import datetime as dt


# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Open the election results and read the file.
electionResults = open(Resources/election_results.csv,r)