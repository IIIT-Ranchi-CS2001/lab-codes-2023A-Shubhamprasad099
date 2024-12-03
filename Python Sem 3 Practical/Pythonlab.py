import pandas as pd
import numpy as np
data = pd.read_csv("AQI_Data.csv")

print(" ")

print("First 5 rows of the dataset are")
print(data.head(5))

print(" ")

print("Last 6 rows of the dataset are:")
print(data.tail(6))

print(" ")

print("Summary of dataset is")
print(data.describe())

print(" ")
print(" The Mean of AQI, PM2.5, PM10")
area = data['City'].unique()
for city in area:
    city_data = data[data['City'] == city]
    print(f"{city}")
    print("Mean of AQI:", np.mean(city_data['AQI']))
    print("Mean of PM2.5", np.mean(city_data['PM2.5']))
    print("Mean of PM10", np.mean(city_data['PM10']))

print(" ")
print(" ")
print("SET 5 Questions")
print(" ")
print("Question 1:-")
print("Extracting data of delhi")
delhi_extract = data[data['City'] == 'Delhi']
print(delhi_extract)
print(" ")

print("Question 2:-")
print("Display 1st 10 column")
print(data[['City', 'AQI', 'PM2.5']].head(10))
print(" ")

print("Question 3:-")
print("AQI>300 and PM10>200")
filterout = data[(data['AQI'] > 300) & (data['PM10'] > 200)]
print(filterout)

