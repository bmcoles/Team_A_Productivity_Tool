""""
This is the basis of displaying graphical data using matplotlib. It will be further incorporated into other modules as needed. This program can take user input or a file input and create graphs from it.
"""
# Add matplotlib to pathway
import sys
sys.path.append(r'C:\\Users\\Zayne\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages')

# create plot from matplotlib
import matplotlib.pyplot as plt

# Create variables for data
x_axis = []
y_axis = []

# Ask user if using a file for input or typing input directly
input_method = int(input("Enter the input method for graph generation:\n1. File\n2. Typed\n:"))

# Use file as input
if input_method == 1:
    filename = str(input("Please enter file name: ")) # get filename
    try:
        #open file and get data
        for line in open(filename, 'r'):
            data = [float(s) for s in line.split()]
            x_axis.append(data[0])
            y_axis.append(data[1])
    except Exception as e:
        print("\nTrouble opening file\n",e)

# Get user enter data    
elif input_method == 2:
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

# Create figure
fig_1, axes = plt.subplots(1, 3, figsize=(10, 15))
# create line plot
axes[0].plot(x_axis, y_axis,'rv--')
axes[0].set_xlabel('x axis')
axes[0].set_ylabel('y axis')
axes[0].set_title("Line Plot")

# create scatter plot
axes[1].scatter(x_axis, y_axis,marker='d')
axes[1].set_xlabel('x axis')
axes[1].set_ylabel('y axis')
axes[1].set_title("Scatter Plot")

# create bar graph
axes[2].bar(x_axis, y_axis,color='y')
axes[2].set_xlabel('x axis')
axes[2].set_ylabel('y axis')
axes[2].set_title("Bar Graph")

plt.show()
