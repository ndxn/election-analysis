# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# MOD 3 CHALLENGE - Initialize string for counties and dictionary for county votes
county_options = []
county_votes = {}
# MOD 3 CHALLENGE - Initialize string for county with most votes
county_with_highest_votes = ""
county_highest_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # print(headers) #Example from Module 3 work to show header row was indeed skipped
    # Print each row in the CSV file. 
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # MOD 3 CHALLENGE - Get the county name from each row
        county_name = row[1]
        # If the county does not match any existing county, add to the county list
        if county_name not in county_options:
            # Add the county name to the county list
            county_options.append(county_name)
            # Begin tracking that county's vote count
            county_votes[county_name] = 0
        # Add vote to that county's total
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Write election results to text file
    txt_file.write(election_results)

    # MOD 3 CHALLENGE - Print out voter turnout by county
    counties_section_header = "\nCounties:\n"
    print(counties_section_header)
    txt_file.write(counties_section_header)
    for county in county_votes:
        # Retrieve vote count and county representation as percentage
        votes = county_votes[county]
        county_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_percentage:.1f}% ({votes:,})\n")
        # Print vote count by county and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        # Determine county vote count, county representation, and county with most votes.
        if (votes > county_highest_count):
            county_highest_count = votes
            county_with_highest_votes = county

    # Print the largest county turnout results to the terminal.
    county_highest_turnout_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {county_with_highest_votes}\n"
        f"-------------------------\n")
    print(county_highest_turnout_summary)
    # Write county highest turnout summart to text file
    txt_file.write(county_highest_turnout_summary)


    # Save the final vote count to the text file.
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

