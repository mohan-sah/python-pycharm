# WAY 1
# with open("weather_data.csv") as weather_data:
#     old_data = weather_data.readlines()
#     data = []
#     for words in old_data:
#         data.append(words.strip())
#     print(data)


# WAY 2
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
# WAY 2.1
#     # old_temperature = []
#     # for row in data:
#     #     old_temperature.append(row[1])
#     #     temperature = old_temperature[1:]
#     # old_temperature = []
#     # for num in temperature:
#     #     old_temperature.append(int(num))
#     #
#     # print(old_temperature)

# WAY 2.2
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


# WAY 3

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data)
# print('\n')
# print(data["temp"])
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

# # series 1-d array functions
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(pd.Series.mean(data["temp"]))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(sum(temp_list)/len(temp_list))

# # get data in column
# print(data["condition"])
# print(data.condition)

# # get data in row
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data.temp.max()])

# # get a particular cell and apply a function
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# #convert C to F temp
# def f(x):
#     x = x*1.8 + 32
#     return x
#
# print(monday.temp.apply(func=f))


# Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")

# creating squirrel count by color of fur
big_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240309.csv")
small_data = big_data["Primary Fur Color"]
print(small_data.unique())
# [nan 'Gray' 'Cinnamon' 'Black']
# WAY 1
# my_squirrel_color_data = small_data.value_counts(dropna=True)
# my_squirrel_color_data.to_csv("my_squirrel_color_data.csv")

# WAY 2
grey_squirrels_count = len(big_data[big_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(big_data[big_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(big_data[big_data["Primary Fur Color"] == "Black"])
data_dict = {
    "squirrel color": ['Gray', 'Cinnamon', 'Black'],
    "count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]

}
df = pd.DataFrame(data_dict)
df.to_csv("another_squirrel_data.csv")
