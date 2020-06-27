import os 
import csv

input_path = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
output_path = os.path.join("..", "PyPoll", "Analysis", "election_results.txt")

print("Election Results")
print("-----------------------")

votes = []
candidates = []

with open(input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        votes.append(row)
        candidates.append(row[2])

    khan_count = candidates.count("Khan")
    correy_count = candidates.count("Correy")
    li_count = candidates.count("Li")
    otooley_count = candidates.count("O'Tooley")

    khan_percent = (khan_count / len(votes))*100
    correy_percent = (correy_count / len(votes))*100
    li_percent = (li_count / len(votes))*100
    otooley_percent = (otooley_count / len(votes)) * 100

    print(f"Total Votes: {len(votes)}")
    print("-----------------------")
    
    # prints out the total vote count and percentage for each candidate.
    print(f"Khan: {round(khan_percent, 4)}% ({khan_count})")
    print(f"Correy: {round(correy_percent, 4)}% ({correy_count})")    
    print(f"Li: {round(li_percent, 4)}% ({li_count})")
    print(f"O'Tooley: {round(otooley_percent, 4)}% ({otooley_count})")
    print("-----------------------")
    print("Winner: Khan")

with open(output_path, "w+") as f:
    f.write("Election Results \n")
    f.write("----------------------- \n")
    f.write(f"Total Votes: {len(votes)} \n")
    f.write("----------------------- \n")
    f.write(f"Khan: {round(khan_percent, 4)}% ({khan_count}) \n")
    f.write(f"Correy: {round(correy_percent, 4)}% ({correy_count}) \n")
    f.write(f"Li: {round(li_percent, 4)}% ({li_count}) \n")
    f.write(f"O'Tooley: {round(otooley_percent, 4)}% ({otooley_count}) \n")
    f.write("----------------------- \n")
    f.write("Winner: Khan")
