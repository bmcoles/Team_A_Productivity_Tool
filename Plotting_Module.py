"""
Json_plotting.py v1.5
This Program takes user input, reads in a json file, and outputs the plot of a specific dataset designated by user

UPDATES:
v1.2: Added safeguards to ensure user can only enter valid input in x and y pairs
v1.3: Addapted to accept only json files as input. Removed code relevant to user input and json
	output writing.
v1.4: updated code to accept a task name and json file
v1.5: Removed unused code and added comments
"""

# Import modules
import matplotlib.pyplot as plot
import json
from json import JSONEncoder
from collections import namedtuple

# Create class for tasks
class task:
	# initialize attributes
	def __init__(self, name, time_frame, time_units, time_axes, target, target_units, target_axes):
		self.name = name			# name of task
		self.time_frame = time_frame		# value for time to complete
		self.time_units = time_units		# units of time to complete task
		self.time_axes = time_axes		# array of time values
		self.target = target			# value of target goal to reach
		self.target_units = target_units	# units of target goal
		self.target_axes = target_axes		# array of target values

# create json decoder for custom class
def taskDecoder(taskDict):
    return namedtuple('X', taskDict.keys())(*taskDict.values()) # converts json data to a list structure

# Get input file
json_file = str(input("\nEnter the file for json input:"))

try: #attempt to open file
    # Read in json_file and plot data as bar graph
    with open(json_file, 'r') as infile:
        importedData = json.load(infile, object_hook=taskDecoder) #load in json data

    # get task to plot
    searchTask = str(input("\nEnter name of task to plot:"))

    # Search for task in importedData
    checker = 0 # variable checking for the existence of task
    index = -1  # index of the task

    # Loop through tasks in task list
    for i in range(0, len(importedData)):
        if importedData[i].task == searchTask:
            checker = 1 #update checekr on a successful match
            index = i   #update index on a successful match

    # plot data if task was found
    if checker != 0:
        taskName = importedData[index].task             # get name of task for plot title
        y_units  = importedData[index].taskUnits        # get units for task
        y_max    = importedData[index].targetGoal       # get the target goal for task completion
        x_units  = importedData[index].timeUnits        # get units of time for completion
        x_max    = importedData[index].timeAmount       # get length of time
        x_raw    = importedData[index].currentTime      # current time data values
        y_raw    = importedData[index].currentProgress  # current progression values

        # Ensure that the number of x points and y points is the same
        if len(x_raw) == len(y_raw):
            # Convert string data to integers
            y_max = int(y_max)  #convert y_max to int
            x_max = int(x_max)  #convert x_max to int

            x_data = [int(s) for s in x_raw]    #convert x values to ints
            y_int = [int(s) for s in y_raw]     #convert y values to ints

            # Adjust y_data to be cumulative
            y_data = []     #create array for updated y values
            run_total = 0   #keeps a running sum of the y values

            # Loop through all y values
            for i in y_int:
                run_total += i              #update running total
                y_data.append(run_total)    #append value to y_data

            # make line graph of data
            fig = plot.figure()                             #create figure variable
            fig.patch.set_facecolor('xkcd:gold')            #set figure color
            ax = fig.add_subplot(1, 1, 1)                   #create axes variable
            ax.set_facecolor('xkcd:silver')                 #set plot background color
            plot.plot(x_data, y_data, 'ko')                 #plot data points (black circles)
            plot.axis([0,x_max,0,y_max])                    #set axes ranges
            plot.title(taskName)                            #set graph title
            plot.xlabel(x_units)                            #set x axes label
            plot.ylabel(y_units)                            #set y axes label
            plot.legend(['Progress'])                       #create legend named 'Progress'
            plot.plot(x_max, y_max,'ro')                    #plot the target goal point
            plot.annotate("Target Goal", (x_max, y_max))    #label target goal point
            plot.show()                                     #display plot
    else: #print line if no task is found
        print("\nThere is no task with name: " + searchTask)
except: #print line if file could not be opened
    print("\nNo file found called: " + json_file)
