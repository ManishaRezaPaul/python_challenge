import os
import csv

# Create path for files to read from the csvfile and write in the textfile
csvpath = os.path.join("Resources","election_data.csv")
textpath = os.path.join("Analysis","Election_Results.txt")

#Set variables
total_votes = 0
candidates = []
candidate_votes = {}
previous_votes = 0
winner = ""
winner_votes = 0

# Open csvfile and textfile to read values and write the analysis:
with open(csvpath,encoding='UTF-8') as csvfile, open(textpath,'w',encoding='UTF-8') as textfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvwriter = csv.writer(textfile, delimiter=",")
    header = next(csvreader)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([])

    #To loop through the rows
    for row in csvreader:

        # Count the rows to calculate the total votes
        total_votes +=1

        # List the candidates
        all_candidates = row[2]

        # If previous_candidate not in the list of existing candidate then store candidate and initialise vote count to 0
        if all_candidates not in candidates:
            candidates.append(all_candidates)
            candidate_votes[all_candidates] = 0
        
        # Add vote count for all the candidates seperately
        candidate_votes[all_candidates] += 1
    
    print()
    print("Election Results")
    print()
    print("----------------------------------------")
    print()
    print(f"Total votes: {total_votes}")
    print()
    print("----------------------------------------")
    print()
    
    csvwriter.writerow([f"Total votes: {total_votes}"])
    csvwriter.writerow([])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([])


    for all_candidates in candidates:
        votes = candidate_votes[all_candidates]
        percent = round((votes / total_votes) * 100, 3)

        if winner_votes < votes:
            winner = all_candidates
            winner_votes = votes
        
        
        print(f"{all_candidates}: {percent}% ({votes})")
        csvwriter.writerow([f"{all_candidates}: {percent}% ({votes})"])
    
    print()
    print("----------------------------------------")
    print()
    print(f"Winner: {winner} {winner_votes}")
    print()
    print("----------------------------------------")

    csvwriter.writerow([])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow([])
    csvwriter.writerow(["----------------------------------------"])
    

        
        
  
    
    

    
    
        
            
    



    
    





