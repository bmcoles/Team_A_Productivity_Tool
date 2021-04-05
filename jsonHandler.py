# The purpose of this program is to take in data from the c shell and process it into a json file
# It will also read in current json files for already created and in-progress tasks
# The purpose of this is to track the progress of all tasks and store information for them for later use
# Authored by Brennan Coles,

# TODO - handle file processing to work with user profiles
# TODO - Clean up code and add better and more descriptive comments

import json
import os

option = 'n'  # Used extensively for the user input
search = 'n'  # Used later for the search feature

while option != 'r' and option != 'w':  # Loop guarantees only valid input is accepted
    option = input("Enter r for read or w for write: ")

while option == 'r' or option == 'w':  # Loop runs only while the user specifies to read and write
    if option == 'r':  # read option
        checker = 'TRUE'
        while checker == 'TRUE':
            try:
                # This 'toRead' will be adjusted to work with the user's profile later
                toRead = input("Enter the full filepath with filename for the file you would like to read: ")
                # C:\\Users\\hyper\\Documents\\data.json
                readData = json.load(open(toRead))
                checker = 'FALSE'
            except IOError:
                print("That file was not found. Please try again.")
                checker = 'TRUE'

        while option != 'a' and option != 's':  # Determines how you read
            option = input("Type a to see all entries or s to search for a specific task: ")
        if option == 'a':  # All entries
            while option != 't' and option != 'f' and option != 'b':  # Distinguish between task and timeframe
                option = input("Type t to see just the tasks, f to see just the time frame, and b for both: ")
            for i in readData:  # Loops through the .json file
                if option == 't':
                    print("task: " + i)
                if option == 'f':
                    print("time frame: " + readData[i])
                if option == 'b':
                    print("task: " + i + ", " + "time frame: " + readData[i])

        if option == 's':  # Search feature
            while option != 'c':
                option = input("enter t to find the time frame for a task or f to find the tasks with a set time frame: ")
                if option == 't':
                    search = input("Type the task you would like to search for: ")
                    for i in readData:
                        if search == i:
                            print("time frame for this task is " + readData[i])

                if option == 'f':
                    search = input("Type the time frame you would like to search for: ")
                    for i in readData:
                        if search == readData[i]:
                            print("the task with this time frame is " + i)

                option = input("type c to quit or any other key to keep searching: ")

        option = input("Type w to write to a file, r to read another file, or any other value to quit: ")

    if option == 'w':  # Write option
        checker = 'TRUE'
        toAdd = 'g'
        data = {}
        # The purpose of this loop is to take input from the user to set up and create a .json file of their tasks
        while option != 'n' and option != 'o':
            option = input("Type n to write to a new file or o to append to an old file: ")

        if option == 'n':
            checker = 'TRUE'
            while toAdd != 'q':
                task = input("Enter the task name: ")
                timeFrame = input("Enter the time frame to complete this task: ")
                data[task] = timeFrame
                toAdd = input("Enter q to quit or any other value to continue: ")

            while checker == 'TRUE':
                toWrite = input("Enter the full filepath (with no filename) for the location you would like to write to: ")
                if os.path.exists(toWrite)==True:
                    checker = 'FALSE'
                else:
                    print("That location is invalid. Try again.")

            toWrite2 = input("Enter the name of the file to create including the .json at the end: ")
            toWrite3 = toWrite+toWrite2
            with open(toWrite3, 'w') as outfile:
                json.dump(data, outfile)


        if option=='o':
            # Loop sets all values currently in readData into data before adding new values to data
            # Runs in O(n) time complexity
            checker = 'TRUE'
            while checker=='TRUE':
                try:
                    toAppend = input("Enter the full filepath with filename for the file you would like to append: ")
                    # C:\\Users\\hyper\\Documents\\data.json
                    readData = json.load(open(toAppend))
                    checker = 'FALSE'
                except IOError:
                    print("That file was not found. Please try again.")
                    checker = 'TRUE'

            for i in readData:
                data[i] = readData[i]
            while toAdd != 'q':
                task = input("Enter the task name: ")
                timeFrame = input("Enter the time frame to complete this task: ")
                data[task] = timeFrame
                toAdd = input("Enter q to quit or any other value to continue: ")
            with open(toAppend, 'w') as outfile:
                json.dump(data, outfile)
        option = input("Type w to write to another file, r to read a file, or any other value to quit: ")
