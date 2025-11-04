


#2. 

#importing the libraries
import pandas as pd 
import matplotlib.pyplot as plt

#loading the data
snelec_data =  pd.read_csv('data/snelec_data.csv')
saowind_data = pd.read_csv('data/saowind_data.csv', skiprows=10)


#checking the data type and ensuring you are dealing with date time object for the dates
snelec_data.info()
saowind_data.info()

#transforming the date column (object) into datetime
snelec_data['Date']= pd.to_datetime(snelec_data['Date'])

#renaming the snelec_data  year, month and day for convenience
saowind_data.columns = ['year', 'month', 'day', 'hour','WS50M', 'WD50M']

#combining seperate year, month , day into date column
saowind_data['Date'] = pd.to_datetime(saowind_data[['year', 'month', 'day', 'hour']])
saowind_data =  saowind_data[['Date','WS50M' , 'WD50M' ]]

#merging both saowind and sne data by date
sahelpow_data = snelec_data.merge(saowind_data , on='Date' ,how='outer')

#for ease in the analysis, getting rid of the missing instances.
sahelpow_data  = sahelpow_data.dropna().reset_index(drop = True)
