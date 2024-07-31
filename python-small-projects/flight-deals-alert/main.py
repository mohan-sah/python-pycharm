from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.getdata()
print(sheet_data)

flight_search = FlightSearch()

for city in sheet_data:
    if city["iataCodes"] == '':
        city["iataCodes"] = flight_search.get_destination_code(city['city'])
print(f"sheet_data:\n {sheet_data}")

data_manager.datarow = sheet_data
data_manager.edit_exiting_record()


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


