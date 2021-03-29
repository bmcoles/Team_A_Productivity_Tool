"""
Json_plotting.py v1.1
This Program takes user input, converts is to a json file, and outputs the plot

"""

# Add matplotlib to pathway
import sys
sys.path.append(r'C:\\Users\\Zayne\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages')

import matplotlib.pyplot as plot
import json

"""            
Create write_json function
This function takes in data and a filename and converts the passed data to json format and stores to the file
"""
def write_json( data, filename ):
    with open(filename, "w") as f:      #open output file
        json.dump(data, f, indent=4)    #write data to file
        
x_axis = []
y_axis = []

json_file = str(input("\nEnter the file for json output:"))

# get x values
x_entries = int(input("Enter number of x values: "))
print("\nEnter x values:\n")
for i in range(0, x_entries):
    entry = int(input())
    x_axis.append(entry)

# get y values
y_entries = int(input("Enter number of y values: "))
print("\nEnter y values:\n")
for i in range(0, y_entries):
    entry = int(input())
    y_axis.append(entry)

# Add current data to to json file
data = {}                   # create data dictionary for json writing
data['x_axis'] = x_axis     # create x_axis variable with data from x_axis
data['y_axis'] = y_axis     # create y_axis variable with data from y_axis

write_json(data, json_file) #write data to output file in local directory

# Read in json_file and plot data as bar graph
with open(json_file, 'r') as infile:
    imported = json.load(infile)

# get x_axis and y_axis data from imported
x_data = []                     # create x_data list
y_data = []                     # create y_data list
x_data = imported['x_axis']     # 
y_data = imported['y_axis']

# make line graph of data
plot.plot(x_data, y_data, 'ro')
plot.axis([0,10,0,20])
plot.show()



