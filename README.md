# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
There were "x" votes cast in the election.
The candidates were:
Candidate 1
Candidate 2
Candidate 3

The candidate results were:

Candidate 1 received "x%" of the vote and "y" number of votes.
Candidate 2 received "x%" of the vote and "y" number of votes.
Candidate 3 received "x%" of the vote and "y" number of votes.
The winner of the election was:

Candidate (1, 2, or 3), who received "x%" of the vote and “y" number of votes.

## Challenge Overview

### NOTES FOR THE APPROACH TO MODULE 3 CHALLENGE
The challenge ask for additional functionality to be added to the code in order to tally votes by county. Because the code already iterated through the csv file, I opted to add the functionality to the existing for loop and if statement which should reduce the amount of time it takes for the program to run. Directly below in the README are the instructions for the challenge. Comments are added therein to explain where the work has been added. 

### Module 3 Requirements

#### 1. Create a list for the counties.
See Line 18
#### 2. Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
See Line 19
#### 3. Create an empty string that will hold the county name that had the largest turnout.
See Line 21
#### 4. Declare a variable that represents the number of votes that a county received.
See line 73. Note that this same variable will be reused in the loop for votes by candidate
#### 5. Inside the with open() function where you are outputting the file, do the following:
##### 5a.Create three if statements to print out the voter turnout results similar to the results shown above.
This starts at line 67 and is accomplished with 1 if statement that is nested in the for loop (runs 3 times)
##### 5b.Add the results to the output file.
Output is done between Lines 67 and 93 alongside printing to the command line
##### 5c.Print the results to the command line.
See 5b 

32 ## Challenge Summary
