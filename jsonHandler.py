# The purpose of this program is to take in data from the c shell and process it into a json file
# It will also read in current json files for already created and in-progress tasks
# The purpose of this is to track the progress of all tasks and store information for them for later use
# Authored by Brennan Coles

# TODO - Add checks for certain user input
# TODO - Clean up (Add more comments, make more clear for the user)

import json
from collections import namedtuple


# Decoder that allows us to use a custom formatted json object
def tasksDecoder(tasksDict):
    return namedtuple('X', tasksDict.keys())(*tasksDict.values())


option = 'n'  # Used extensively for the user input
search = 'n'  # Used later for the search feature

# Loop guarantees only valid input is accepted
while option != 'r' and option != 'w' and option != 'u' and option != 'd':
    option = input("Enter r for read, w for write, u to update data for progress on a task, or d to delete a task: ")

# Loop runs only while the user specifies to read and write
while option == 'r' or option == 'w' or option == 'u' or option == 'd':

    # read option
    if option == 'r':

        checker = 'TRUE'
        # Checker is used to guarantee a valid file location is selected.
        # If the user types in an invalid file, they are prompted to try again.
        while checker == 'TRUE':
            try:
                toRead = input("Enter the name for the file you would like to read: ")
                toRead = "C:\\Users\\hyper\\Documents\\" + toRead + ".json"
                readData = json.load(open(toRead))
                checker = 'FALSE'
            except IOError:
                print("That file was not found. Please try again.")
                checker = 'TRUE'

        # Converts our file to the custom json object
        with open(toRead, 'r') as file:
            theData = file.read().replace('\n', '')
        readTasks = json.loads(theData, object_hook=tasksDecoder)

        # Specifies read options search and all.
        # Loops until valid input is received.
        while option != 'a' and option != 's':
            option = input("Type a to see all entries or s to search for a specific task: ")

        # Search all entries
        if option == 'a':
            # Distinguish between task and timeframe data points
            while option != 't' and option != 'f' and option != 'b':
                option = input("Type t to see just the tasks, f to see just the time frame, and b for both: ")

                if option == 't':
                    i = len(readTasks)
                    j = 0
                    while j < i:
                        print(readTasks[j].task, readTasks[j].targetGoal, readTasks[j].taskUnits)
                        j = j + 1

                if option == 'f':
                    i = len(readTasks)
                    j = 0
                    while j < i:
                        print(readTasks[j].timeAmount, readTasks[j].timeUnits)
                        j = j + 1

                if option == 'b':
                    i = len(readTasks)
                    j = 0
                    while j < i:
                        print(readTasks[j].task, readTasks[j].targetGoal, readTasks[j].taskUnits,
                              readTasks[j].timeAmount, readTasks[j].timeUnits)
                        j = j + 1

        # Search feature
        if option == 's':
            while option != 'c':
                # Option always us to search for specific tasks or time frames
                option = input(
                    "enter t to find the time frame for a task or f to find the tasks with a set time frame: ")

                if option == 't':
                    search = input("Type of the task you would like to search for (no amount): ")
                    i = len(readTasks)
                    j = 0
                    k = 0
                    finder = ''
                    while j < i:
                        finder = readTasks[j].task
                        if search == finder:
                            k = j
                            j = i
                        j = j + 1
                    print(readTasks[k].timeAmount, readTasks[k].timeUnits)

                if option == 'f':
                    search = input("Type of the timeframe you would like to search for (no amount): ")
                    search2 = input("Amount for this timeframe: ")
                    i = len(readTasks)
                    j = 0
                    k = 0
                    finder = ''
                    while j < i:
                        finder = readTasks[j].timeUnits
                        finder = readTasks[j].timeAmount
                        if search == finder:
                            k = j
                            j = i
                        j = j + 1
                    print(readTasks[k].task, readTasks[k].targetGoal, readTasks[k].taskUnits)

                option = input("type c to quit or any other key to keep searching: ")

            option = input(
                "Type w to write to a file, r to read another file, u to update an entry, d to delete a task, or any other value to quit: ")

    # Update progress option
    if option == 'u':

        checker = 'TRUE'
        # Checker is used to guarantee a valid file location is selected.
        # If the user types in an invalid file, they are prompted to try again.
        while checker == 'TRUE':
            try:
                toRead = input("What file holds the task you would like to update?: ")
                toRead = "C:\\Users\\hyper\\Documents\\" + toRead + ".json"
                readData = json.load(open(toRead))
                checker = 'FALSE'
            except IOError:
                print("That file was not found. Please try again.")
                checker = 'TRUE'

        # Converts our file to the custom json object
        with open(toRead, 'r') as file:
            theData = file.read().replace('\n', '')
        readTasks = json.loads(theData, object_hook=tasksDecoder)

        task = input("Enter the task you would like to update an entry for: ")
        i = len(readTasks)
        j = 0
        k = 0
        l = 0
        finder = ''
        while j < i:
            finder = readTasks[j].task
            if search == finder:
                k = j
                j = i
            j = j + 1

        currentT = []
        currentP = []

        print("The allotted time frame for this task is ", readTasks[k].timeAmount, readTasks[k].timeUnits)
        i = len(readTasks[k].currentTime)
        if i == 0:
            print("You currently have no entries for this task.")
        if i > 0:
            print("Your current entries for this task are: ")
            while l < i:
                print(readTasks[k].currentTime[l], readTasks[k].currentProgress[l])
                currentT.extend([readTasks[k].currentTime[l]])
                currentP.extend([readTasks[k].currentProgress[l]])
                l = l + 1
        option = 'y'

        while option == 'y':
            new = input("Enter the current time: ")
            new2 = input("Enter the current progress: ")
            currentT.extend([new])
            currentP.extend([new2])
            option = ("Enter y to enter another value or any other character to not: ")

        appendData = []

        m = len(readTasks)
        j = 0
        while j < m:
            if j != k:
                appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                    "targetGoal": readTasks[j].targetGoal,
                                    "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                    "currentTime": readTasks[j].currentTime,
                                    "currentProgress": readTasks[j].currentProgress}])
            else:
                appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                    "targetGoal": readTasks[j].targetGoal,
                                    "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                    "currentTime": currentT,
                                    "currentProgress": currentP}])
            j = j + 1

        with open(toRead, 'w') as outfile:
            json.dump(appendData, outfile)

        option = input(
            "Type w to write to a file, r to read another file, u to update an entry, do to delete a task, or any other value to quit: ")

    # Delete Option
    if option == 'd':
        checker = 'TRUE'
        # Checker is used to guarantee a valid file location is selected.
        # If the user types in an invalid file, they are prompted to try again.
        while checker == 'TRUE':
            try:
                toRead = input("What file holds the task you would like to update?: ")
                toRead = "C:\\Users\\hyper\\Documents\\" + toRead + ".json"
                readData = json.load(open(toRead))
                checker = 'FALSE'
            except IOError:
                print("That file was not found. Please try again.")
                checker = 'TRUE'

        # Converts our file to the custom json object
        with open(toRead, 'r') as file:
            theData = file.read().replace('\n', '')
        readTasks = json.loads(theData, object_hook=tasksDecoder)

        taskToDelete = input("Enter the task you would like to delete an entry for: ")

        appendData = []
        m = len(readTasks)
        j = 0
        while j < m:

            if readTasks[j].task != taskToDelete:
                appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                    "targetGoal": readTasks[j].targetGoal,
                                    "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                    "currentTime": readTasks[j].currentTime,
                                    "currentProgress": readTasks[j].currentProgress}])
            j = j + 1
        print(appendData)

        with open(toRead, 'w') as outfile:
            json.dump(appendData, outfile)

        option = input(
            "Type w to write to a file, r to read another file, u to update an entry, do to delete a task, or any other value to quit: ")

    # Write option
    if option == 'w':
        checker = 'TRUE'
        toAdd = 'g'
        data = []

        # This loop guarantees only proper input is received.
        while option != 'n' and option != 'o':
            option = input("Type n to write to a new file or o to append to an old file: ")

        # New file option.
        if option == 'n':
            checker = 'TRUE'
            while toAdd != 'q':
                task = input("Enter the task type: ")
                task2 = input("Enter the task units: ")
                task3 = input("Enter the task amount: ")
                timeFrame = input("Enter the time frame type for this task (week, day, month, etc.): ")
                timeFrame2 = input("Enter the time frame amount: ")
                data.extend([{"task": task, "taskUnits": task2, "targetGoal": task3, "timeUnits": timeFrame,
                              "timeAmount": timeFrame2, "currentTime": [], "currentProgress": []}])
                toAdd = input("Enter q to quit or any other value to continue: ")

            toWrite = input("Enter the name of the file you would like to write: ")
            toWrite = "C:\\Users\\hyper\\Documents\\" + toWrite + ".json"

            with open(toWrite, 'w') as outfile:
                json.dump(data, outfile)

        # Append to old file option
        if option == 'o':
            checker = 'TRUE'
            while checker == 'TRUE':
                try:
                    toAppend = input("Enter the name of the file to append: ")
                    toAppend = "C:\\Users\\hyper\\Documents\\" + toAppend + ".json"
                    readData = json.load(open(toAppend))
                    checker = 'FALSE'
                except IOError:
                    print("That file was not found. Please try again.")
                    checker = 'TRUE'

            with open(toAppend, 'r') as file:
                theData = file.read().replace('\n', '')
            fileToAppend = json.loads(theData, object_hook=tasksDecoder)

            appendData = []

            i = len(fileToAppend)
            j = 0
            while j < i:
                appendData.extend([{"task": fileToAppend[j].task, "taskUnits": fileToAppend[j].taskUnits,
                                    "targetGoal": fileToAppend[j].targetGoal,
                                    "timeUnits": fileToAppend[j].timeUnits, "timeAmount": fileToAppend[j].timeAmount,
                                    "currentTime": fileToAppend[j].currentTime,
                                    "currentProgress": fileToAppend[j].currentProgress}])
                j = j + 1

            while toAdd != 'q':
                task = input("Enter the task name: ")
                task2 = input("Enter the task amount: ")
                task3 = input("Enter the task units: ")
                timeFrame = input("Enter the time frame type for this task (week, day, month, etc.): ")
                timeFrame2 = input("Enter the amount for this time frame: ")

                appendData.extend([{"task": task, "taskUnits": task2, "targetGoal": task3, "timeUnits": timeFrame,
                                    "timeAmount": timeFrame2, "currentTime": [], "currentProgress": []}])

                toAdd = input("Enter q to quit or any other value to continue: ")
            with open(toAppend, 'w') as outfile:
                json.dump(appendData, outfile)
        option = input(
            "Type w to write to a file, r to read another file, u to update an entry, or any other value to quit: ")
