# The purpose of this program is to take in data from the c shell and process it into a json file
# It will also read in current json files for already created and in-progress tasks
# The purpose of this is to track the progress of all tasks and store information for them for later use
# Authored by Brennan Coles, ADD AS YOU WORK ON IT

# TODO - Get program integrated with c shell instead of standing alone

import json

option = 'n' # Used extensively for the user input
search = 'n' # Used later for the search feature

while option !='r' and option !='w': # Loop guarantees only valid input is accepted
    option = input ("Enter r for read or w for write: ")

while option == 'r' or option == 'w': # Loop runs only while the user specifies to read and write
    if option == 'r':
        readData =json.load(open('C:\\Users\\hyper\\Documents\\data.json'))
        while (option != 'a' and option !='s'):
            option = input("Type a to see all entries or s to search for a specific task: ")
        if (option == 'a'):
            while (option !='t' and option !='f' and option !='b'):
                option = input ("Type t to see just the tasks, f to see just the time frame, and b for both: ")
            for i in readData:
                if (option == 't'):
                    print(i)
                if (option == 'f'):
                    print(readData[i])
                if (option == 'b'):
                    print(i + " " + readData[i])
        if (option == 's'):
            # TODO Implement the search feature
            print("NOT IMPLEMENTED YET")
            # while (option != 'c'):
                 #search = input("Type the task you would like to search for")

        option = input("Type w to write to a file, r to read another file, or any other value to quit: ")

    if option == 'w':
        toAdd = 'g';
        data = {}  # Will be named User_data
        # The purpose of this loop is to take input from the user to set up and create a .json file of their tasks
        while toAdd != 'q':
            # TODO - Configure input to work with the c shell
            task = input("Enter the task name: ")
            timeFrame = input("Enter the time frame to complete this task: ")
            data[task] = timeFrame
            toAdd = input("Enter q to quit or any other value to continue: ")
        with open('C:\\Users\\hyper\\Documents\\data.json', 'w') as outfile:
            json.dump(data, outfile)
        option = input("Type w to write to another file, r to read a file, or any other value to quit: ")
