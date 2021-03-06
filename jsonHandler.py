# This program reads and processes data in .json format based on user interaction
# At the most basic level it reads and writes to files
# More specific commands allow it to search for specific tasks or append to existing files
# Other commands for different purposes exist as well
# The data is formatted to interact with Zayne's graphing program
# Authored by Brennan Coles

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

                # The loops below for each option will go through the entire object
                # What they grab depends on what the user has specified
                # All created files during writing will be formatted the same way

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
            option = input("Type w to write to a file, r to read another file, u to update an entry, d to delete a task, or any other value to quit: ")

        # Search feature
        if option == 's':
            while option != 'c':
                # Option always us to search for specific tasks or time frames
                option = input("enter t to find the time frame for a task or f to find the tasks with a set time frame: ")

                # The loops below also go through the entire object
                # They will stop when the proper entry is found
                # Tracker variables are used to note the correct location
                # Found is used to loop back if a nonexistent entry is entered
                
                found = False
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
                            found = True
                        j = j + 1
                    if found == True:
                        print(readTasks[k].timeAmount, readTasks[k].timeUnits)

                if option == 'f':
                    search = input("Type of the timeframe you would like to search for (week, month, etc.): ")
                    search2 = input("Amount for this timeframe (10, 50, etc.): ")
                    i = len(readTasks)
                    j = 0
                    k = 0
                    finder = ''
                    while j < i:
                        finder = readTasks[j].timeUnits
                        finder2 = readTasks[j].timeAmount
                        if search == finder and search2 == finder2:
                            k = j
                            j = i
                            found = True
                        j = j + 1
                    if found == True:
                        print(readTasks[k].task, readTasks[k].targetGoal, readTasks[k].taskUnits)

                if found == False:
                    print("Entry not found!")
                option = input("type c to quit or any other key to keep searching: ")

            option = input("Type w to write to a file, r to read another file, u to update an entry, d to delete a task, or any other value to quit: ")

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

        # The loop below finds the correct task to update
        # Does so by using tracker variables to not position
        # of the proper entry in the object and file
        # Found is used to loop back if a non existent entry is entered
        found = False
        task = input("Enter the task you would like to update an entry for: ")
        i = len(readTasks)
        j = 0
        k = 0
        l = 0
        finder = ''
        while j < i:
            finder = readTasks[j].task
            if task == finder:
                k = j
                j = i
                found = True
            j = j + 1

        # These will be used later to store the new data points
        currentT = []
        currentP = []
        if found == True:
            print("The allotted time frame for this task is", readTasks[k].timeAmount, readTasks[k].timeUnits)
            i = len(readTasks[k].currentTime)
            if i == 0:
                print("You currently have no entries for this task.")
            if i > 0:
                print("Your current entries for this task are: ")
                while l < i:
                    print(readTasks[k].timeUnits, readTasks[k].currentTime[l], '-', readTasks[k].currentProgress[l], readTasks[k].taskUnits)
                    # These extend functions will add existing data to our storage created earlier
                    currentT.extend([readTasks[k].currentTime[l]])
                    currentP.extend([readTasks[k].currentProgress[l]])
                    l = l + 1
            option = 'y'

            while option == 'y':
                
                # Checker2 used to make sure only numeric input is received below
                checker2 = True
                while checker2:
                    try:
                        checker2 = False
                        new = input("Enter the value for the current time for this task (numeric amount only) : ")
                        toCheck = int(new)
                    except ValueError:
                        print("This value is not numeric. Enter again.")
                        checker2 = True

                checker2 = True
                while checker2:
                    try:
                        checker2 = False
                        new2 = input("Enter the value for the  current progress for this task (numeric amount only): ")
                        toCheck = int(new2)
                    except ValueError:
                        print("This value is not numeric. Enter again.")
                        checker2 = True
                currentT.extend([new])
                currentP.extend([new2])
                option = input ("Enter y to enter another value or any other character to not: ")

            # Data is appended together her to merge the old and new values
            appendData = []

            # The loop below goes through all of the old tasks and re-adds them to the appended data
            m = len(readTasks)
            j = 0
            while j < m:
                # Checks to see if we are on the entry we are adding new information to
                if j != k:
                    appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                        "targetGoal": readTasks[j].targetGoal,
                                        "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                        "currentTime": readTasks[j].currentTime,
                                        "currentProgress": readTasks[j].currentProgress}])
                # This else will add in the new data in addition to the new for the task that needs to be updated
                else:
                    appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                        "targetGoal": readTasks[j].targetGoal,
                                        "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                        "currentTime": currentT,
                                        "currentProgress": currentP}])
                j = j + 1

            with open(toRead, 'w') as outfile:
                json.dump(appendData, outfile)

        if found == False:
            print ("Entry to update not found!")
        option = input("Type w to write to a file, r to read another file, u to update an entry, d to delete a task, or any other value to quit: ")

    # Delete Option
    if option == 'd':
        checker = 'TRUE'
        # Checker is used to guarantee a valid file location is selected.
        # If the user types in an invalid file, they are prompted to try again.
        while checker == 'TRUE':
            try:
                toRead = input("What file holds the task you would like to delete?: ")
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
        print ("Would you like to delete the entire entry or just some previously entered progress?")
        option = input ("Enter e for entire or p for some progress: ")

        if option == 'e':
            # This will store all of our old data minus what we delete
            appendData = []
            m = len(readTasks)
            j = 0
            while j < m:
                # Every value will be re-added to the new array sans what we are removing
                if readTasks[j].task != taskToDelete:
                    appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                        "targetGoal": readTasks[j].targetGoal,
                                        "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                        "currentTime": readTasks[j].currentTime,
                                        "currentProgress": readTasks[j].currentProgress}])
                j = j + 1

            with open(toRead, 'w') as outfile:
                json.dump(appendData, outfile)

        if option == 'p':
            # This will store all of our old data minus what we delete
            appendData = []
            currentT = []
            currentP = []
            m = len(readTasks)
            j = 0
            while j < m:
                # Every value will be re-added to the new array sans what we are removing
                if readTasks[j].task != taskToDelete:
                    appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                        "targetGoal": readTasks[j].targetGoal,
                                        "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                        "currentTime": readTasks[j].currentTime,
                                        "currentProgress": readTasks[j].currentProgress}])
                else:
                    n = len(readTasks[j].currentTime)
                    o = 0
                    print("Your current entries for this task are: ")
                    while o<n:
                        print(readTasks[j].timeUnits, readTasks[j].currentTime[o], '-', readTasks[j].currentProgress[o], readTasks[j].taskUnits)
                        option = input ("Type y if you would like to delete this entry or any other character if not: ")
                        if option != 'y':
                            currentT.extend([readTasks[j].currentTime[o]])
                            currentP.extend(readTasks[j].currentProgress[o])
                        o = o + 1
                    appendData.extend([{"task": readTasks[j].task, "taskUnits": readTasks[j].taskUnits,
                                        "targetGoal": readTasks[j].targetGoal,
                                        "timeUnits": readTasks[j].timeUnits, "timeAmount": readTasks[j].timeAmount,
                                        "currentTime": currentT,
                                        "currentProgress": currentP}])

                j = j + 1
            with open(toRead, 'w') as outfile:
                json.dump(appendData, outfile)

        option = input("Type w to write to a file, r to read another file, u to update an entry, d to delete a task, or any other value to quit: ")

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
                task = input("Enter the type of task without units (lose weight, write a book, etc.): ")
                task2 = input("Enter the task units (lbs, pages, etc.): ")
                checker2 = True
                while checker2:
                    try:
                        checker2 = False
                        task3 = input("Enter the task amount (10, 50, etc.): ")
                        toCheck = int(task3)
                    except ValueError:
                        print("This value is not numeric. Enter again.")
                        checker2 = True
                timeFrame = input("Enter the time frame type for this task (week, day, etc.): ")
                checker2 = True
                while checker2:
                    try:
                        checker2 = False
                        timeFrame2 = input("Enter the time frame amount (5, 10, etc.): ")
                        toCheck = int(timeFrame2)
                    except ValueError:
                        print("This value is not numeric. Enter again.")
                        checker2 = True
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
                task = input("Enter the type of task without units (lose weight, write a book, etc.): ")
                task2 = input("Enter the task units (lbs, pages, etc.): ")
                checker2 = True
                while checker2:
                    try:
                        checker2 = False
                        task3 = input("Enter the task amount (10, 50, etc.): ")
                        toCheck = int(task3)
                    except ValueError:
                        print("This value is not numeric. Enter again.")
                        checker2 = True
                timeFrame = input("Enter the time frame type for this task (week, day, etc.): ")
                checker2 = True
                while checker2:
                    try:
                        checker2 = False
                        timeFrame2 = input("Enter the time frame amount (5, 10, etc.): ")
                        toCheck = int(timeFrame2)
                    except ValueError:
                        print("This value is not numeric. Enter again.")
                        checker2 = True

                appendData.extend([{"task": task, "taskUnits": task2, "targetGoal": task3, "timeUnits": timeFrame,
                                    "timeAmount": timeFrame2, "currentTime": [], "currentProgress": []}])

                toAdd = input("Enter q to quit or any other value to continue: ")
            with open(toAppend, 'w') as outfile:
                json.dump(appendData, outfile)
        option = input("Type w to write to a file, r to read another file, u to update an entry, or any other value to quit: ")
