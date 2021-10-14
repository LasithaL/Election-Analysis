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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the csv file
    #for row in file_reader:
    #    print(row)


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