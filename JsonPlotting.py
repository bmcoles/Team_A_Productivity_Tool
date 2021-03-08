"""
Json_plotting.py v0.1
This program is a stand alone to work on taking json files and importing and plotting the data

It will take the input file from the last program and convert it to json format, save it as a json file, then open it, read it, and plot it
"""

import matplotlib.pyplot as plot
import json

"""            
Create write_json function
This function takes in data and a filename and converts the passed data to json format and stores to the file
"""
def write_json( data, filename ):
    with open(filename, "w") as f:      #open output file
        json.dump(data, f, indent=4)    #write data to file
        
#Take input from file and convert to json
filename = str(input("Enter the file name: ")) # get file name
try:
    #open the input file
    for line in open(filename, 'r'):
        indata = [float(s) for s in line.split()] # read data by row into data matrix
        x_axis.append(indata[0]) # add data in first column to x axis list
        y_axis.append(indata[1]) # add data in second column to y axis list
except Exception as e:
        print("\nTrouble opening file\n",e)

json_file = str(input("\nEnter the file for json output\n"))

# Add current data to to json file
data = [x_axis, y_axis] # make x and y axis dat as one list
write_json(data, json_file) #write data to output file in local directory

# Read in json_file and plot data as bar graph
with open(json_file, 'r') as infile:
    imported = json.load(infile)

# get x_axis and y_axis data from imported
x_data = imported['x_axis']
y_data = imported['y_axis']

# make line graph of data
plot.plot(x_data, y_data, 'ro')
plot.axis([0,6,0,20])



