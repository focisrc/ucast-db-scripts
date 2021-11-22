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
import datetime as dt
# import astropy.units as u
# from astropy.time import Time
# from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_sun

#Opacity of scatter plot markers
Alpha = 0.1

#Type of marker used in scatter plot
Marker = '.'

#Creating empty figure, and creating axes
fig = plt.figure()
ax = plt.axes()

#Defining path to data files that will be analyzed, and a path where the plots you create will be saved.

#Data starts on 05/12/2003

# path = 'KP12M_data_new.csv'
outpath = 'data_plots_year_round/Tau_data/'

dataRead=pd.read_csv('EHT_Weather_CSV_Files/SMT_data_edit.csv', header=0)
tauRead=dataRead['tau']
SMTtau=tauRead.to_numpy()
whenRead=dataRead['dateStart']
whenSMT=pd.to_datetime(whenRead)
SMTdate=whenSMT.to_numpy()
date_index = dataRead.set_index(['dateStart'])
# data = date_index.loc['2003-09-01':'2019-09-17']
# print(data)

#Need to read in times as well

data = []
#Year
for i in range(2004,2019):
	#Month
	for j in range(1, 12):
		#Day
		for k in range(1, 31):
			if j == 2 and k == 28:
				data.append(date_index.loc[str(i)+'-' + str(j) + '-' + str(k) :str(i)+'-' + str(j+1) + '-01'])

			if j == 4 or 6 or 9 or 11 and k == 30:
				data.append(date_index.loc[str(i)+'-' + str(j) + '-' + str(k) :str(i)+'-' + str(j+1) + '-01'])
			if j == 1 or 2 or 3 or 5 or 7 or 10 or 12 and k == 31:
				data.append(date_index.loc[str(i)+'-' + str(j) + '-' + str(k) :str(i)+'-' + str(j+1) + '-01'])
			else:
				data.append(date_index.loc[str(i)+'-' + str(j) + '-' + str(k) :str(i)+'-' + str(j) + '-' + str(k + 1)])
	# data_02 = date_index.loc[str(i)+'-12-15':str(i)+'-12-16']
	# data_03 = date_index.loc[str(i)+'-12-16':str(i)+'-12-17']
	# data_04 = date_index.loc[str(i)+'-12-17':str(i)+'-12-18']
	# data_05 = date_index.loc[str(i)+'-12-18':str(i)+'-12-19']
	# data_06 = date_index.loc[str(i)+'-12-19':str(i)+'-12-20']
	# data_07 = date_index.loc[str(i)+'-12-20':str(i)+'-12-21']
	# data_08 = date_index.loc[str(i)+'-12-21':str(i)+'-12-22']
	# data_09 = date_index.loc[str(i)+'-12-22':str(i)+'-12-23']
	# data_10 = date_index.loc[str(i)+'-12-23':str(i)+'-12-24']
	# data_11 = date_index.loc[str(i)+'-12-24':str(i)+'-12-25']
	# data_12 = date_index.loc[str(i)+'-12-25':str(i)+'-12-26']
	# data_13 = date_index.loc[str(i)+'-12-26':str(i)+'-12-27']
	# data_14 = date_index.loc[str(i)+'-12-27':str(i)+'-12-28']
	
				array = np.array(data['tau'])
	# array2 = np.array(data_02['tau'])
	# array3 = np.array(data_03['tau'])
	# array4 = np.array(data_04['tau'])
	# array5 = np.array(data_05['tau'])
	# array6 = np.array(data_06['tau'])
	# array7 = np.array(data_07['tau'])
	# array8 = np.array(data_08['tau'])
	# array9 = np.array(data_09['tau'])
	# array10 = np.array(data_10['tau'])
	# array11 = np.array(data_11['tau'])
	# array12 = np.array(data_12['tau'])
	# array13 = np.array(data_13['tau'])
	# array14 = np.array(data_14['tau'])
				print(array1.shape)
	# print(array.shape)

				x = np.linspace(0, len(array1), num = len(array1))
	# x2 = np.linspace(0, len(array2), num = len(array2))
	# x3 = np.linspace(0, len(array3), num = len(array3))
	# # x4 = np.linspace(0, len(array4), num = len(array4))
	# # x5 = np.linspace(0, len(array5), num = len(array5))
	# # x6 = np.linspace(0, len(array6), num = len(array6))
	# x7 = np.linspace(0, len(array7), num = len(array7))
	# x8 = np.linspace(0, len(array8), num = len(array8))
	# x9 = np.linspace(0, len(array9), num = len(array9))
	# x10 = np.linspace(0, len(array10), num = len(array10))
	# x11 = np.linspace(0, len(array11), num = len(array11))
	# x12 = np.linspace(0, len(array12), num = len(array12))
	# x13 = np.linspace(0, len(array13), num = len(array13))
	# x14 = np.linspace(0, len(array14), num = len(array14))

	#Allowing each of the filenames data set to have its own scatter plot
				plt.scatter(x, array, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x2, array2, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x3, array3, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# # plt.scatter(x4, array4, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# # plt.scatter(x5, array5, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# # plt.scatter(x6, array6, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x7, array7, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x8, array8, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x9, array9, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x10, array10, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x11, array11, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x12, array12, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x13, array13, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	# plt.scatter(x14, array14, c = 'blue', alpha = Alpha, marker = Marker, s = 8)
	
ax.set_xticks([12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288])
ax.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
plt.title('Tau over 14 day interval (12_14 - 12_27) from 2004-2019')
plt.xlabel('Hours', size = 12)
plt.ylabel('Optical Depth (Tau)', size = 12)
plt.tick_params(direction = 'in')
ax.grid()
# plt.savefig(outpath + 'tau_14day_1214_1227_2004_to_2019.png', bbox_inches = 'tight')
plt.show()
# month_day_parse = dataRead.loc['09/01':'09/16']
# print(SMTdate)

print('Read SMT data')

# parser = lambda date: pd.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
# read_data = pd.read_csv('KP12M_data_new.csv', skiprows = 195708, usecols = [1, 10], parse_dates = [1], date_parser = parser, header = None)
# df = pd.DataFrame({'date': read_data[0], 'Tau': read_data[1]})
# print(df)
# read_data.columns = ['date', 'Tau']
# month_day = read_data.set_index([0])
# month_day = read_data.loc['2004-09-01 00:00:00':'2004-09-17 00:00:00']
# print(month_day)