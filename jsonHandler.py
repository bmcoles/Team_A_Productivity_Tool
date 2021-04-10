# The purpose of this program is to take in data from the c shell and process it into a json file
# It will also read in current json files for already created and in-progress tasks
# The purpose of this is to track the progress of all tasks and store information for them for later use
# Authored by Brennan Coles,

# TODO - handle file processing to work with user profiles (quick change)
# TODO - Add the ability to delete entries
# TODO - Add checks for certain user input

import json
import os

option = 'n'  # Used extensively for the user input
search = 'n'  # Used later for the search feature

# Loop guarantees only valid input is accepted
while option != 'r' and option != 'w':
    option = input("Enter r for read or w for write: ")

# Loop runs only while the user specifies to read and write
while option == 'r' or option == 'w':
    # read option
    if option == 'r':
        checker = 'TRUE'
        # Checker is used to guarantee a valid file location is selected.
        # If the user types in an invalid file, they are prompted to try again.
        while checker == 'TRUE':
            try:
                # toRead, as well as readData, are for the task data points.
                toRead = input("Enter the name for the file you would like to read: ")
                # toRead2, as well as readData2, are for the associated timeFrame data points.
                toRead2 = "C:\\Users\\hyper\\Documents\\" + toRead + "2" + ".json"
                toRead = "C:\\Users\\hyper\\Documents\\" + toRead + ".json"
                readData = json.load(open(toRead))
                readData2 = json.load(open(toRead2))
                checker = 'FALSE'
            except IOError:
                print("That file was not found. Please try again.")
                checker = 'TRUE'

        # Specifies read options search and all.
        # Loops until valid input is received.
        while option != 'a' and option != 's':
            option = input("Type a to see all entries or s to search for a specific task: ")
        # Search all entries
        if option == 'a':
            # Distinguish between task and timeframe data points
            while option != 't' and option != 'f' and option != 'b':
                option = input("Type t to see just the tasks, f to see just the time frame, and b for both: ")

                # All of the for loops in their respective if statements parse
                # through the file with the correct data points
                # And print the relevant information.
                if option == 't':
                    for i in readData:
                        print("task: " + i + ", " + "how much: " + readData[i])

                if option == 'f':
                    for i in readData2:
                        print("time frame type: " + i + ", " + "how much: " + readData2[i])

                # To print both, both files need to be accessed simultaneously.
                # Because of how .json is stored, loaded, and read, there must be two loops
                # to access the files. h and j allow us to grab the associated timeframe data
                # for the correct task data. h goes up and tracks where we are in tasks,
                # while j, which is always reset, tracks timeframe. Since timeframe is
                # accessed within the inner loop, j must be reset everytime. When h and j match,
                # we know we have the two data points that go with each other.
                if option == 'b':
                    h = 0
                    j = 0
                    for i in readData:
                        j = 0
                        for m in readData2:
                            if h == j:
                                print("task: " + i +  ", " + "how much: " + readData[i] + ", " + "time frame type: " + m + ", " + "how much: " + readData2[m])
                            j = j+1
                        h = h+1

        # Search feature
        if option == 's':
            while option != 'c':
                # Option always us to search for specific tasks or time frames
                option = input("enter t to find the time frame for a task or f to find the tasks with a set time frame: ")

                if option == 't':
                    search = input("Type of the task you would like to search for (no amount): ")
                    m = 0
                    # Since we access both files, and use an inner loop,
                    # We go through using the same method above for
                    # option b of the all feature.
                    for i in readData:
                        if search == i:
                            m2 = 0
                            for g in readData2:
                                if m == m2:
                                    print("time frame type for this task: " + g + ", " + "how much: " + readData2[g])
                                m2 = m2+1
                        m = m+1

                # Since we access both files, and use an inner loop,
                # We go through using the same method above for
                # option b of the all feature.
                if option == 'f':
                    search = input("Type of the time frame you would like to search for: ")
                    search2 = input("Amount of the time frame you would like to search for: ")
                    m = 0
                    for i in readData2:
                        if search == i and search2 == readData2[i]:
                            m2 = 0
                            for g in readData:
                                if m == m2:
                                    print("task with this time frame: " + g + ", " + "amount: " + readData[g])
                                m2 = m2+1
                        m = m+1

                option = input("type c to quit or any other key to keep searching: ")

        option = input("Type w to write to a file, r to read another file, or any other value to quit: ")

    # Write option
    if option == 'w':
        checker = 'TRUE'
        toAdd = 'g'
        data = {}
        data2 = {}

        # This loop guarantees only proper input is received.
        while option != 'n' and option != 'o':
            option = input("Type n to write to a new file or o to append to an old file: ")

        # New file option.
        if option == 'n':
            checker = 'TRUE'
            while toAdd != 'q':
                task = input("Enter the task type: ")
                task2 = input("Enter the task amount: ")
                timeFrame = input("Enter the time frame type for this task (week, day, month, etc.): ")
                timeFrame2 = input("Enter the time frame amount: ")
                data[task] = task2
                data2[timeFrame] = timeFrame2
                toAdd = input("Enter q to quit or any other value to continue: ")

            toWrite = input("Enter the name of the file you would like to write: ")
            toWrite2 = "C:\\Users\\hyper\\Documents\\" + toWrite + "2" + ".json"
            toWrite = "C:\\Users\\hyper\\Documents\\" + toWrite + ".json"

            with open(toWrite, 'w') as outfile:
                json.dump(data, outfile)

            with open(toWrite2, 'w') as outfile:
                json.dump(data2, outfile)

        # Append to old file option
        if option=='o':
            # Loop sets all values currently in readData into data before adding new values to data
            # Runs in O(n) time complexity
            checker = 'TRUE'
            while checker=='TRUE':
                try:
                    toAppend = input("Enter the name of the file to append: ")
                    toAppend2 = "C:\\Users\\hyper\\Documents\\" + toAppend + "2" + ".json"
                    toAppend = "C:\\Users\\hyper\\Documents\\" + toAppend + ".json"
                    readData = json.load(open(toAppend))
                    readData2 = json.load(open(toAppend2))
                    checker = 'FALSE'
                except IOError:
                    print("That file was not found. Please try again.")
                    checker = 'TRUE'

            for i in readData:
                data[i] = readData[i]
            for i in readData2:
                data2[i] = readData2[i]
            while toAdd != 'q':
                task = input("Enter the task name: ")
                task2 = input("Enter the task amount: ")
                timeFrame = input("Enter the time frame type for this task (week, day, month, etc.): ")
                timeFrame2 = input("Enter the amount for this time frame: ")
                data[task] = task2
                data2[timeFrame] = timeFrame2
                toAdd = input("Enter q to quit or any other value to continue: ")
            with open(toAppend, 'w') as outfile:
                json.dump(data, outfile)
            with open(toAppend2, 'w') as outfile:
                json.dump(data2, outfile)
        option = input("Type w to write to another file, r to read a file, or any other value to quit: ")

