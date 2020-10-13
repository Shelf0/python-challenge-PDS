# Start with Importing the CSV file
import csv

csv_filepath = "C:/Users/19739/Desktop/Data Science/RUT-SOM-DATA-PT-09-2020-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

# Create a dictionary for the candidates
candidate_dictionary = {}

#set variables & counters for votes
total_votes = 0
max_popular_votes = 0
winner = ""

#Open CSV file to start manipulating data

with open(csv_filepath) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        total_votes += 1
        #This Calculates the Number of total votes^
        candidates_name = row[2]
        # This uses each candidates name as a key to attach values
        # If the candidates name is present on the candidate_dictionary, it will increment the corresponding value by 1
        # Otherwise, the default value will be 0 and we increment that by 1
        candidate_dictionary[candidates_name] = candidate_dictionary.get(candidates_name, 0) + 1


# This for loop iterates over the key,value pairings in the candidate dictionary
# And finds out who has the max popular votes, and then sets the winner based on that
for (k, v) in candidate_dictionary.items():
    if (v > max_popular_votes) :
        max_popular_votes = v
        winner = k

#This prints the election results
print('Election Results')
print('-' * 25)
#this prints the total votes
print(f'Total Votes: {total_votes}')
#This Calculates Total votes for Khan
print('-' * 25)
#This Prints Total Votes For Khan
print("Khan: {:.3f}% ({})".format(round(candidate_dictionary["Khan"]/total_votes * 100, 3), candidate_dictionary["Khan"]))
#This Prints Total votes for Correy
print("Correy: {:.3f}% ({})".format(round(candidate_dictionary["Correy"]/total_votes * 100, 3), candidate_dictionary["Correy"]))
#This Prints Total votes for Li
print("Li: {:.3f}% ({})".format(round(candidate_dictionary["Li"]/total_votes * 100, 3), candidate_dictionary["Li"]))
#This Prints Total Votes for O'Tooley
print("O'Tooley: {:.3f}% ({})".format(round(candidate_dictionary["O'Tooley"]/total_votes * 100, 3), candidate_dictionary["O'Tooley"]))
print('-' * 25)
print(f'Winner: {winner}')
print('-' * 25)