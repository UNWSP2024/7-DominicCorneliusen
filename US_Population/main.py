#Title: US Population
#Author: Dominic Corneliusen
#Date last modified: 3/6/2026

#Start
def get_data():
    year = int(input("Enter a year: "))
    state = input("Enter a state: ")
    population = int(input("Enter a population: "))
    new_list = [year, state, population]
    return new_list
amount_of_lists = int(input("How much data are you entering? "))
data = []
while amount_of_lists > 0:
    data.append(get_data())
    amount_of_lists -= 1
year = int(input("Now, enter a year. "))
total_population = 0
for entry in data:
    if entry[0] == year:
        total_population += entry[2]
print("Total population for", year, "is", total_population)