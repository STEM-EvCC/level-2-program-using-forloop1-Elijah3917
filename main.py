mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

year_count = 0
success_count = 0
success_rate = 0


# Loop counting based on mission names
for i in range(len(mission_years)):
    year_count += 1
    if(mission_success[i] == True):
        success_count += 1

# Getting the success rate/rounding it
success_rate = (success_count / year_count) * 100 
round_success = f'{success_rate:.2f}'

# Print results
print("Total number of missions: " + str(year_count))
print("Number of successful missions: 5")
print("Success rate: " + round_success + "%")

# Using a for loop to display missions launched
print("Missions launched before the year 2000:")
for i in range(len(mission_years)):
    if(mission_years[i] < 2000):
        print("- " + mission_names[i])