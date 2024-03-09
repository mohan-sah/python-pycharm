
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
        #WAY 2.1
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

data = pd.read_csv("weather_data.csv")
print(data)
print('\n')
# print(data["temp"])
# print(type(data["temp"]))
data_dict = data.to_dict()
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
monday = data[data.day == "Monday"]
print(monday.condition)

#convert C to F temp
def f(x):
    x = x*1.8 + 32
    return x

print(monday.temp.apply(func=f))





