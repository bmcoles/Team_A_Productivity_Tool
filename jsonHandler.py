# The purpose of this program is to take in data from the c shell and process it into a json file
# It will also read in current json files for already created and in-progress tasks
# The purpose of this is to track the progress of all tasks and store information for them for later use
# Authored by Brennan Coles, ADD AS YOU WORK ON IT

import json

# TODO - offer modality based on shell inputs to either add to the data file or access existing tasks

# TODO - implement commands to parse the read file
with open('path_to_file/data.json') as file:
  read_Data = json.load(file)


# Data storage for our tasks
# Could be formatted as 'task':'time_passed'
# Alternatively could be 'task':'time_remaining' for time sensitive goals
# TODO - figure out how to read in data passed from the c shell and pass it to the data object
# TODO - figure out how to use the name of the user in the 'data' object name

data = {} # Will be named User_data
data['tasks'] = []
data['tasks'].append({

# EXAMPLE
    # 'Lose 10 pounds':'One week'

})

# Stores the data to an output file
with open ('data.json', 'w') as outfile:
    json.dump(data, outfile)
