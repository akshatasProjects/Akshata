import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature_list = []
    for eachRow in data:
        if eachRow[1] != "temp":
           temperature_list.append(int(eachRow[1]))
    print(temperature_list) 