#This code is to create a graphical display of any data downloaded from Kitt Peaks Weather data (located at:
# http://modelo.as.arizona.edu:8080/plot/maser_temps/1/today) as a function of time using a csv/tsv file or txt file. 
#Here, this script is being used to plot optical depth, Tau, over time. 
#Sean Dougall
#V1.0.0
#Updates: None at Moment


#Importing libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sci 
import os

#Opacity of scatter plot markers
Alpha = 0.1

#Type of marker used in scatter plot
Marker = '.'

#Creating empty figure, and creating axes
fig = plt.figure()
ax = plt.axes()

#Defining path to data files that will be analyzed, and a path where the plots you create will be saved.
path = '15_day_increments/'
outpath = 'data_plots/'

#Listing the files in the directory "path"
file_path = os.listdir(path)

#Creating a for loop that will process through the filenames and read the data within each file. Each data file will be parsed
#using the np.loadtxt() function, where the data column seperation can be specified using the delimter=. Columns to be
#used within an array can also be specified using the usecols=, where here, I am calling upon the 2nd column.
print(path)
for file_name in file_path[0:25]:
	filename = path + str(file_name)
	print(path) 
	data = np.loadtxt(filename, delimiter = '\t', usecols = 1)
	#Defining the y data points
	y_data = data

	#Creating the x data points with same length as the y data, and evenly spaced. For the Tau data, each point on the x axis
	#represents 5 minutes
	x = np.linspace(0, len(y_data), num = len(y_data))

	#Allowing each of the filenames data set to have its own scatter plot
	plt.scatter(x, y_data, c = 'blue', alpha = Alpha, marker = Marker, s = 8)

#Setting tick marks, here each value represents the number of data points it takes to reach each day, since each point
#for Tau vs time is 5 minutes, each tick will be a day further, or 288 points further. Also this is setting tick labels 
#to describe the time in days. The rest is plotting.
ax.set_xticks([288, 576, 864, 1152, 1440, 1728, 2016, 2304, 2592, 2880, 3168, 3456, 3744, 4032, 4320, 4608])
ax.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
plt.title('Tau over 16 day interval (09_2020 - 09_2021)')
plt.xlabel('Days', size = 12)
plt.ylabel('Optical Depth (Tau)', size = 12)
plt.tick_params(direction = 'in')
ax.grid()
plt.savefig(outpath + '2019_09_2020_09_1year.png', bbox_inches = 'tight')
plt.show()
