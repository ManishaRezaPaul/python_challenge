# python_challenge
Repo for Week 3 Python module challenge

## Ensuring filepath works!
This included setting a path for both (csvfile & textfile) files and ensuring the files are available in the specified location. To ensure that the code for the specific challenge runs smoothly, need to ensure that the terminal location is set to the specific (PyBank or PyPoll) folders.

## PyBank Challenge
In this activity we used the csv read and write functions to read data from csv file, conduct analysis of the Profit/Losses over a seven year period and write the analysis in a textfile. 

### Challenge objective
This challenge required to calculate the [total_months], [total_amount], [change_over_the_entire_period] & [average_change], [greatest_increase] and [greatest_decrease] in Profits".

### Conducting analysis from the dataset
1. Used the [with] statement to open and close the dataset to conduct the analysis

2. Used the [for] (loop) function for the following calculation: 
    To calculate the [total_months] (by counting the rows)
    To calculate the [total_amount] of Profit/Losses, (by calculating the values in column 2)

3. Used the [if] (conditional) statements function for the following calculation:
    To calculate the [change_over_the_entire_period] (which helps in calculating the [average_change])
    To find the [greatest_increase] and [greatest_decrease] in the Profit/Losses


## PyPoll Challenge
In this activity we used the csv read and write functions to read data from csv file, produce election results and write the results in a textfile

### Challenge objective
This challenge required to calculate the [total_votes], [candidate_list], [candidate_votes_percentage] & [candidate_votes] and [election_winner].

### Calculating results from the dataset
1. Used {} to create dictionary of all the candidates

2. Used the [with] statement to open and close the dataset to calculate the results

3. Used the [for] (loop) function for the following calculation:
    To calculate the [total_votes], (by counting the rows)
    To gather information for the [candidate_votes_percentage] & [candidate_votes]

4. Used the [if] (conditional) statements for the following calculation:
    To collect [candidate_list] 
    To find the [election_winner]

5. Used "in" and "not in" operators to check for votes for each candidates 


**[+=] helps to add to the existing values to calculate the total months and total amount accurately

### Printing and writing values in terminal and textfile
Used print(f" {}") to include the results of all the analysis in the terminal
Used csvwrite.writerow([f" {}"]) to include the results of all the analysis in the textfile
