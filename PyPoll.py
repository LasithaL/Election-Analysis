# What we need to pull form the data set.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The total number of votes each candidate received.
# 4. Percentage of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Adding the dependencies
import os
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Add and initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

# Candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    #print(headers)
    
    # Print each row in the csv file
    for row in file_reader:
        #print(row)
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in  candidate_votes:
        # Retrieve vote count for candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidates name and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the if the vote is > winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate = candidate's name.
            winning_candidate = candidate_name

    # Winning candidate summary.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n")
    print(winning_candidate_summary)
    

# Print the candidate vote dictionary.
#print(candidate_votes)

# Print the candidate list
#print(candidate_options)

# 3. Print the total votes
#print(total_votes)



# Create a filename variable to a direct or indirect path to the file.


# Using the open() function with the "w" mode we will write data to the file.
#out_file = open(file_to_save, "w")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    #txt_file.write("Hello World")

    # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    # txt_file.write("Counties in the Election")
    # txt_file.write("\n-------------------------")
    # txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
#out_file.close()