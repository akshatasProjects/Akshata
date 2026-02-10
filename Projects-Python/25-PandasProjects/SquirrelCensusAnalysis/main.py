import pandas

data = pandas.read_csv("2018_Squirrel_Data.csv")

# Accessing the "Fur Color" Column in CSV file and get the data in Row
gray_squirrel_count = len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"]=="Black"])



# Creating the new Data frame using the above info
data_dict = {"Fur Color":["Gray","Cinnamon","Black"],
             "Count":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]   
            }
dataFrame = pandas.DataFrame(data_dict)

# Saving the above data to CSV file by creating new file
dataFrame.to_csv("count_of_squirrel.csv")