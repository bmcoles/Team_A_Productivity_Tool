# The purpose of this program is to take in data from the c shell and process it into a json file
# It will also read in current json files for already created and in-progress tasks
# The purpose of this is to track the progress of all tasks and store information for them for later use
# Authored by Brennan Coles, ADD AS YOU WORK ON IT
# General TODO - Get program integrated with c shell instead of standing alone
import json

# TODO - Configure the options to work with c shell input
option = 'n'
option = input ("Enter r for read or w for write: ")

while option == 'r' or option == 'w':
    if option == 'r':
        # TODO - Configure the open statement to take data passed in from the c shell
        f = open('C:\\Users\\hyper\\Documents\\data.json')
        readData = json.load(f)
        for i in readData['tasks']:
            print(i)
        option = input("Type w to write to a file, r to read another file, or any other value to quit: ")


    if option == 'w':
        toAdd = 'g';
        data = {} # Will be named User_data
        data['tasks'] = []
        # The purpose of this loop is to take input from the user to set up and create a .json file of their tasks
        while toAdd != 'q':
            # EXAMPLE
            # 'Lose 10 pounds':'One week'
            # TODO - Configure input to work with the c shell
            task = input("Enter the task name: ")
            timeFrame = input("Enter the time frame to complete: ")
            data['tasks'].append({
                "task" : task,
                "timeFrame" : timeFrame
            })
            toAdd = input("Enter q to quit or any other value to continue: ")

        # Stores the data to an output file
        with open ('C:\\Users\\hyper\\Documents\\data.json', 'w') as outfile:
            json.dump(data, outfile)
        option = input("Type w to write to another file, r to read a file, or any other value to quit: ")
